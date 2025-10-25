#!/usr/bin/env python3
"""
Database Setup Script for Dotsh Monitoring
This script will create/reset the database and seed initial data
"""

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import sys

# CONFIGURATION - UPDATE THESE VALUES
DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'user': 'postgres',  # Change to your PostgreSQL username
    'password': 'admin',  # Change to your PostgreSQL password
    'database': 'dotsh_monitoring'
}

def create_database():
    """Create the database if it doesn't exist"""
    try:
        # Connect to PostgreSQL server
        conn = psycopg2.connect(
            host=DB_CONFIG['host'],
            port=DB_CONFIG['port'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            database='postgres'
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        
        # Check if database exists
        cursor.execute(
            "SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s",
            (DB_CONFIG['database'],)
        )
        exists = cursor.fetchone()
        
        if not exists:
            cursor.execute(f"CREATE DATABASE {DB_CONFIG['database']}")
            print(f"✓ Database '{DB_CONFIG['database']}' created successfully!")
        else:
            print(f"✓ Database '{DB_CONFIG['database']}' already exists")
        
        cursor.close()
        conn.close()
        return True
        
    except Exception as e:
        print(f"✗ Error creating database: {e}")
        return False

def execute_sql_file(filename):
    """Execute SQL commands from a file"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        with open(filename, 'r') as f:
            sql_commands = f.read()
        
        cursor.execute(sql_commands)
        conn.commit()
        cursor.close()
        conn.close()
        
        print(f"✓ SQL file '{filename}' executed successfully!")
        return True
        
    except FileNotFoundError:
        print(f"✗ SQL file '{filename}' not found!")
        return False
    except Exception as e:
        print(f"✗ Error executing SQL: {e}")
        return False

def create_tables_directly():
    """Create tables using direct SQL"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        # Drop existing tables if needed
        print("\nDropping existing tables...")
        cursor.execute("""
            DROP TABLE IF EXISTS services_new CASCADE;
            DROP TABLE IF EXISTS servers_new CASCADE;
            DROP TABLE IF EXISTS project_environments CASCADE;
            DROP TABLE IF EXISTS projects CASCADE;
            DROP TABLE IF EXISTS alerts CASCADE;
            DROP TABLE IF EXISTS server_capacity CASCADE;
            DROP TABLE IF EXISTS servers CASCADE;
            DROP TABLE IF EXISTS users CASCADE;
        """)
        
        print("Creating tables...")
        
        # Users table
        cursor.execute("""
            CREATE TABLE users (
                id SERIAL PRIMARY KEY,
                email VARCHAR(120) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        
        # Servers table
        cursor.execute("""
            CREATE TABLE servers (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                status VARCHAR(20) DEFAULT 'online',
                cpu INTEGER DEFAULT 0,
                memory INTEGER DEFAULT 0,
                uptime VARCHAR(50),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        
        # Server capacity table
        cursor.execute("""
            CREATE TABLE server_capacity (
                id SERIAL PRIMARY KEY,
                server_id INTEGER REFERENCES servers(id) ON DELETE CASCADE,
                total_storage VARCHAR(50),
                used_storage VARCHAR(50),
                available_storage VARCHAR(50),
                storage_percentage INTEGER,
                cpu_cores INTEGER,
                cpu_usage INTEGER,
                total_ram VARCHAR(50),
                ram_usage INTEGER,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        
        # Alerts table
        cursor.execute("""
            CREATE TABLE alerts (
                id SERIAL PRIMARY KEY,
                server_id INTEGER REFERENCES servers(id) ON DELETE CASCADE,
                alert_type VARCHAR(50),
                message VARCHAR(255),
                severity VARCHAR(20),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        
        # Projects table
        cursor.execute("""
            CREATE TABLE projects (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                description TEXT,
                owner VARCHAR(100),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        
        # Project environments table
        cursor.execute("""
            CREATE TABLE project_environments (
                id SERIAL PRIMARY KEY,
                project_id INTEGER REFERENCES projects(id) ON DELETE CASCADE,
                environment_type VARCHAR(20) NOT NULL CHECK (environment_type IN ('dev', 'stage', 'prod')),
                region VARCHAR(50),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        
        # Servers new table
        cursor.execute("""
            CREATE TABLE servers_new (
                id SERIAL PRIMARY KEY,
                environment_id INTEGER REFERENCES project_environments(id) ON DELETE CASCADE,
                name VARCHAR(100) NOT NULL,
                ip_address VARCHAR(50),
                os VARCHAR(100),
                status VARCHAR(20) DEFAULT 'online',
                cpu_cores INTEGER,
                cpu_usage INTEGER DEFAULT 0,
                ram VARCHAR(50),
                ram_usage INTEGER DEFAULT 0,
                storage VARCHAR(50),
                storage_used INTEGER DEFAULT 0,
                uptime VARCHAR(50),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        
        # Services new table
        cursor.execute("""
            CREATE TABLE services_new (
                id SERIAL PRIMARY KEY,
                server_id INTEGER REFERENCES servers_new(id) ON DELETE CASCADE,
                name VARCHAR(100) NOT NULL,
                port VARCHAR(50),
                status VARCHAR(20) DEFAULT 'online',
                response_time VARCHAR(20)
            );
        """)
        
        # Create indexes
        cursor.execute("""
            CREATE INDEX idx_servers_status ON servers(status);
            CREATE INDEX idx_servers_new_status ON servers_new(status);
            CREATE INDEX idx_alerts_severity ON alerts(severity);
            CREATE INDEX idx_alerts_created_at ON alerts(created_at DESC);
            CREATE INDEX idx_project_environments_type ON project_environments(environment_type);
        """)
        
        conn.commit()
        cursor.close()
        conn.close()
        
        print("✓ All tables created successfully!")
        return True
        
    except Exception as e:
        print(f"✗ Error creating tables: {e}")
        return False

def verify_tables():
    """Verify that all tables were created"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
            ORDER BY table_name;
        """)
        
        tables = cursor.fetchall()
        cursor.close()
        conn.close()
        
        print("\n" + "="*50)
        print("Tables in database:")
        print("="*50)
        for table in tables:
            print(f"  ✓ {table[0]}")
        print("="*50 + "\n")
        
        return True
        
    except Exception as e:
        print(f"✗ Error verifying tables: {e}")
        return False

def main():
    print("="*50)
    print("Dotsh Monitoring - Database Setup")
    print("="*50 + "\n")
    
    # Step 1: Create database
    print("Step 1: Creating database...")
    if not create_database():
        sys.exit(1)
    
    # Step 2: Create tables
    print("\nStep 2: Creating tables...")
    if not create_tables_directly():
        sys.exit(1)
    
    # Step 3: Verify tables
    print("\nStep 3: Verifying tables...")
    if not verify_tables():
        sys.exit(1)
    
    print("="*50)
    print("Database setup completed successfully!")
    print("="*50)
    print("\nNext steps:")
    print("1. Update app.py with your database credentials")
    print("2. Run: python app.py")
    print("3. Login with: admin@dotsh.com / admin123")
    print("="*50 + "\n")

if __name__ == '__main__':
    # Check if user wants to proceed
    response = input("This will DROP and RECREATE all tables. Continue? (yes/no): ")
    if response.lower() in ['yes', 'y']:
        main()
    else:
        print("Setup cancelled.")