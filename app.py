# app.py - Complete Dotsh Monitoring Application
from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import secrets
import json

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Database configuration
# IMPORTANT: Update with your PostgreSQL credentials
# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/dotsh_monitoring'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ==========================================
# DATABASE MODELS
# ==========================================

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Server(db.Model):
    __tablename__ = 'servers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default='online')
    cpu = db.Column(db.Integer, default=0)
    memory = db.Column(db.Integer, default=0)
    uptime = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class ServerCapacity(db.Model):
    __tablename__ = 'server_capacity'
    id = db.Column(db.Integer, primary_key=True)
    server_id = db.Column(db.Integer, db.ForeignKey('servers.id'), nullable=False)
    total_storage = db.Column(db.String(50))
    used_storage = db.Column(db.String(50))
    available_storage = db.Column(db.String(50))
    storage_percentage = db.Column(db.Integer)
    cpu_cores = db.Column(db.Integer)
    cpu_usage = db.Column(db.Integer)
    total_ram = db.Column(db.String(50))
    ram_usage = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    server = db.relationship('Server', backref='capacity')

class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    owner = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    environments = db.relationship('ProjectEnvironment', backref='project', lazy=True, cascade='all, delete-orphan')

class ProjectEnvironment(db.Model):
    __tablename__ = 'project_environments'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    environment_type = db.Column(db.String(20), nullable=False)  # dev, stage, prod
    region = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    servers = db.relationship('ServerNew', backref='environment', lazy=True, cascade='all, delete-orphan')

class ServerNew(db.Model):
    __tablename__ = 'servers_new'
    id = db.Column(db.Integer, primary_key=True)
    environment_id = db.Column(db.Integer, db.ForeignKey('project_environments.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    ip_address = db.Column(db.String(50))
    os = db.Column(db.String(100))
    status = db.Column(db.String(20), default='online')
    cpu_cores = db.Column(db.Integer)
    cpu_usage = db.Column(db.Integer, default=0)
    ram = db.Column(db.String(50))
    ram_usage = db.Column(db.Integer, default=0)
    storage = db.Column(db.String(50))
    storage_used = db.Column(db.Integer, default=0)
    uptime = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    services = db.relationship('ServiceNew', backref='server', lazy=True, cascade='all, delete-orphan')

class ServiceNew(db.Model):
    __tablename__ = 'services_new'
    id = db.Column(db.Integer, primary_key=True)
    server_id = db.Column(db.Integer, db.ForeignKey('servers_new.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    port = db.Column(db.String(50))
    status = db.Column(db.String(20), default='online')
    response_time = db.Column(db.String(20))

class Alert(db.Model):
    __tablename__ = 'alerts'
    id = db.Column(db.Integer, primary_key=True)
    server_id = db.Column(db.Integer, db.ForeignKey('servers.id'), nullable=False)
    alert_type = db.Column(db.String(50))
    message = db.Column(db.String(255))
    severity = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    server = db.relationship('Server', backref='alerts')

# ========================================
# Add these models to your app.py
# ========================================

class CapacityDataProd(db.Model):
    __tablename__ = 'capacity_data_prod'
    __table_args__ = {'schema': 'public'}
    
    name = db.Column('Name', db.String(255), primary_key=True)
    cpu_overcommit_ratio = db.Column("CPU|Current Overcommit Ratio", db.Float)
    cpu_usable_cores = db.Column("CPU|Number of usable CPUs (Cores)", db.Integer)
    cpu_demand_highest_workload = db.Column("CPU|Demand|Highest Host Workload (%)", db.Float)
    cpu_worst_vm_ready = db.Column("CPU|Worst VM CPU Ready (%)", db.String(255))
    cpu_demand_percent = db.Column("CPU|Demand (%)", db.Float)
    memory_usable_capacity = db.Column("Memory|Usable Capacity", db.Float)
    memory_allocated_consumers = db.Column("Memory|Memory Allocated on all Powered On Consumers", db.Float)
    memory_consumed = db.Column("Memory|Consumed", db.Float)
    memory_overcommit_ratio = db.Column("Memory|Current Overcommit Ratio", db.Float)
    disk_usable_capacity_ha_buffer = db.Column("Disk Space|Allocation|Usable Capacity after HA and Buffer", db.Float)
    disk_total_capacity = db.Column("Disk Space|Total Capacity", db.Float)
    disk_total_provisioned = db.Column("Disk Space|Total Provisioned Disk Space", db.Float)
    disk_utilization = db.Column("Disk Space|Utilization", db.Float)
    disk_overcommit_ratio = db.Column("Disk Space|Current Overcommit Ratio", db.Float)
    vsphere_tag = db.Column("Summary|vSphere Tag", db.String(255))

class CapacityDataStage(db.Model):
    __tablename__ = 'capacity_data_stage'
    __table_args__ = {'schema': 'public'}
    
    name = db.Column('Name', db.String(255), primary_key=True)
    cpu_overcommit_ratio = db.Column("CPU|Current Overcommit Ratio", db.Float)
    cpu_usable_cores = db.Column("CPU|Number of usable CPUs (Cores)", db.Integer)
    cpu_demand_highest_workload = db.Column("CPU|Demand|Highest Host Workload (%)", db.Float)
    cpu_worst_vm_ready = db.Column("CPU|Worst VM CPU Ready (%)", db.String(255))
    cpu_demand_percent = db.Column("CPU|Demand (%)", db.Float)
    memory_usable_capacity = db.Column("Memory|Usable Capacity", db.Float)
    memory_allocated_consumers = db.Column("Memory|Memory Allocated on all Powered On Consumers", db.Float)
    memory_consumed = db.Column("Memory|Consumed", db.Float)
    memory_overcommit_ratio = db.Column("Memory|Current Overcommit Ratio", db.Float)
    disk_usable_capacity_ha_buffer = db.Column("Disk Space|Allocation|Usable Capacity after HA and Buffer", db.Float)
    disk_total_capacity = db.Column("Disk Space|Total Capacity", db.Float)
    disk_total_provisioned = db.Column("Disk Space|Total Provisioned Disk Space", db.Float)
    disk_utilization = db.Column("Disk Space|Utilization", db.Float)
    disk_overcommit_ratio = db.Column("Disk Space|Current Overcommit Ratio", db.Float)
    vsphere_tag = db.Column("Summary|vSphere Tag", db.String(255))


# ========================================
# Add these models to your app.py (after existing models)
# ========================================

class LobInventory1(db.Model):
    __tablename__ = 'lob_inventory1'
    __table_args__ = {'schema': 'public'}
    
    id = db.Column(db.Integer, primary_key=True)
    lob = db.Column(db.String)
    ito_unit = db.Column(db.String)
    itam_ciid = db.Column(db.String)
    app_instance = db.Column(db.String)
    tso = db.Column(db.String)
    tso_status = db.Column(db.String)
    compute_config = db.Column(db.Text)
    canonic_alias = db.Column(db.String)
    name = db.Column(db.String)
    ip_address = db.Column(db.String)
    infra = db.Column(db.String)
    cidr = db.Column(db.String)
    function = db.Column(db.String)
    warn_orphan = db.Column(db.String)
    decomm_after = db.Column(db.DateTime)
    decomm_source = db.Column(db.String)
    decomm_comment = db.Column(db.String)
    vc_vm_poweredoff_at_or_before = db.Column(db.DateTime)
    type = db.Column(db.String)
    size = db.Column(db.String)
    vcpu = db.Column(db.Integer)
    memory_gb = db.Column(db.Integer)
    warn_vm_size = db.Column(db.String)
    product_mf = db.Column(db.String)
    vm_image = db.Column(db.String)
    error_vm_image = db.Column(db.String)
    canonic_alias_fqdn = db.Column(db.String)
    fqdn = db.Column(db.String)
    infoblox_network_infra = db.Column(db.String)
    config_canonic_id = db.Column(db.String)
    serial_number = db.Column(db.String)
    cmdb_ci_sat_signoff = db.Column(db.String)
    cmdb_ci_env = db.Column(db.String)
    cmdb_ci_op_status = db.Column(db.String)
    warn_vm_shipped_folder = db.Column(db.String)
    vc_vm_folder_full = db.Column(db.String)
    vcf_domain = db.Column(db.String)
    vc_cluster = db.Column(db.String)
    vc_cluster_function = db.Column(db.String)
    vc_vm_creation_ts = db.Column(db.DateTime)
    mf_disks_total_gb = db.Column(db.Integer)
    vc_vm_disks_total_gb = db.Column(db.Integer)
    mf_disks = db.Column(db.String)
    vc_vm_disks = db.Column(db.String)
    vc_vm_size = db.Column(db.String)
    vc_vm_vcpu = db.Column(db.Integer)
    vc_vm_memory_gb = db.Column(db.Integer)
    vc_vm_reservations = db.Column(db.String)
    env = db.Column(db.String)
    vip_host_name = db.Column(db.String)
    vip_host_ref = db.Column(db.String)
    vip_host_infra = db.Column(db.String)
    lb_cname_name = db.Column(db.String)
    lb_cname_ref = db.Column(db.String)
    vc_vm_annotation = db.Column(db.Text)
    guest_collect_ts = db.Column(db.DateTime)
    guest_ip_address = db.Column(db.String)
    guest_power_state = db.Column(db.String)
    guest_id = db.Column(db.String)
    guest_tools_running_status = db.Column(db.String)
    guest_tools_status = db.Column(db.String)
    vc_cluster_az = db.Column(db.String)
    vc_vm_instance_uuid = db.Column(db.String)
    vc_vm_id = db.Column(db.String)
    cmdb_ci_sys_id = db.Column(db.String)
    cmdb_ci_first_discovered = db.Column(db.DateTime)
    cmdb_ci_last_discovered = db.Column(db.DateTime)
    infoblox_ref = db.Column(db.String)
    infoblox_network_ref = db.Column(db.String)
    mac_address = db.Column(db.String)
    host_record_name = db.Column(db.String)
    error_image_os = db.Column(db.String)
    import_timestamp = db.Column(db.DateTime)
    state = db.Column(db.String)


class LobInventoryStg(db.Model):
    __tablename__ = 'lob_inventory1_stage'
    __table_args__ = {'schema': 'public'}
    
    id = db.Column(db.Integer, primary_key=True)
    lob = db.Column(db.String)
    ito_unit = db.Column(db.String)
    itam_ciid = db.Column(db.String)
    app_instance = db.Column(db.String)
    tso = db.Column(db.String)
    tso_status = db.Column(db.String)
    compute_config = db.Column(db.Text)
    canonic_alias = db.Column(db.String)
    name = db.Column(db.String)
    ip_address = db.Column(db.String)
    infra = db.Column(db.String)
    cidr = db.Column(db.String)
    function = db.Column(db.String)
    warn_orphan = db.Column(db.String)
    decomm_after = db.Column(db.DateTime)
    decomm_source = db.Column(db.String)
    decomm_comment = db.Column(db.String)
    vc_vm_poweredoff_at_or_before = db.Column(db.DateTime)
    type = db.Column(db.String)
    size = db.Column(db.String)
    vcpu = db.Column(db.Integer)
    memory_gb = db.Column(db.Integer)
    warn_vm_size = db.Column(db.String)
    product_mf = db.Column(db.String)
    vm_image = db.Column(db.String)
    error_vm_image = db.Column(db.String)
    canonic_alias_fqdn = db.Column(db.String)
    fqdn = db.Column(db.String)
    infoblox_network_infra = db.Column(db.String)
    config_canonic_id = db.Column(db.String)
    serial_number = db.Column(db.String)
    cmdb_ci_sat_signoff = db.Column(db.String)
    cmdb_ci_env = db.Column(db.String)
    cmdb_ci_op_status = db.Column(db.String)
    warn_vm_shipped_folder = db.Column(db.String)
    vc_vm_folder_full = db.Column(db.String)
    vcf_domain = db.Column(db.String)
    vc_cluster = db.Column(db.String)
    vc_cluster_function = db.Column(db.String)
    vc_vm_creation_ts = db.Column(db.DateTime)
    mf_disks_total_gb = db.Column(db.Integer)
    vc_vm_disks_total_gb = db.Column(db.Integer)
    mf_disks = db.Column(db.String)
    vc_vm_disks = db.Column(db.String)
    vc_vm_size = db.Column(db.String)
    vc_vm_vcpu = db.Column(db.Integer)
    vc_vm_memory_gb = db.Column(db.Integer)
    vc_vm_reservations = db.Column(db.String)
    env = db.Column(db.String)
    vip_host_name = db.Column(db.String)
    vip_host_ref = db.Column(db.String)
    vip_host_infra = db.Column(db.String)
    lb_cname_name = db.Column(db.String)
    lb_cname_ref = db.Column(db.String)
    vc_vm_annotation = db.Column(db.Text)
    guest_collect_ts = db.Column(db.DateTime)
    guest_ip_address = db.Column(db.String)
    guest_power_state = db.Column(db.String)
    guest_id = db.Column(db.String)
    guest_tools_running_status = db.Column(db.String)
    guest_tools_status = db.Column(db.String)
    vc_cluster_az = db.Column(db.String)
    vc_vm_instance_uuid = db.Column(db.String)
    vc_vm_id = db.Column(db.String)
    cmdb_ci_sys_id = db.Column(db.String)
    cmdb_ci_first_discovered = db.Column(db.DateTime)
    cmdb_ci_last_discovered = db.Column(db.DateTime)
    infoblox_ref = db.Column(db.String)
    infoblox_network_ref = db.Column(db.String)
    mac_address = db.Column(db.String)
    host_record_name = db.Column(db.String)
    error_image_os = db.Column(db.String)
    import_timestamp = db.Column(db.DateTime)
    state = db.Column(db.String)


# ========================================
# UPDATED ROUTES - Replace existing routes
# ========================================

@app.route('/projects')
def projects():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    
    # Get unique LOBs from both prod and stage
    prod_lobs = db.session.query(LobInventory1.lob).distinct().filter(LobInventory1.lob.isnot(None)).all()
    stage_lobs = db.session.query(LobInventoryStg.lob).distinct().filter(LobInventoryStg.lob.isnot(None)).all()
    
    # Combine and create unique list of projects
    all_lobs = set([lob[0] for lob in prod_lobs] + [lob[0] for lob in stage_lobs])
    
    # Create project list with environment counts
    projects_list = []
    for lob in sorted(all_lobs):
        prod_count = LobInventory1.query.filter_by(lob=lob).count()
        stage_count = LobInventoryStg.query.filter_by(lob=lob).count()
        
        # Get first record to get additional info
        sample_prod = LobInventory1.query.filter_by(lob=lob).first()
        sample_stage = LobInventoryStg.query.filter_by(lob=lob).first()
        
        sample = sample_prod or sample_stage
        
        projects_list.append({
            'id': lob,  # Using LOB name as ID
            'name': lob,
            'description': f'Infrastructure for {lob}',
            'owner': sample.tso if sample and sample.tso else 'Unknown',
            'created_at': sample.import_timestamp if sample and sample.import_timestamp else datetime.utcnow(),
            'has_prod': prod_count > 0,
            'has_stage': stage_count > 0,
            'prod_count': prod_count,
            'stage_count': stage_count,
            'total_count': prod_count + stage_count
        })
    
    return render_template('projects_lob.html', projects=projects_list)


@app.route('/project/<project_id>')
def project_detail(project_id):
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    
    # Fetch servers from both prod and stage for this LOB
    prod_servers = LobInventory1.query.filter_by(lob=project_id).all()
    stage_servers = LobInventoryStg.query.filter_by(lob=project_id).all()
    
    # Prepare environment data
    environments_data = []
    
    # Production Environment
    if prod_servers:
        env_dict = {
            'id': 'prod',
            'type': 'prod',
            'region': 'Production',
            'servers': []
        }
        
        for server in prod_servers:
            server_dict = {
                'id': server.id,
                'name': server.name or server.canonic_alias or 'Unknown',
                'ip_address': server.ip_address or server.guest_ip_address,
                'fqdn': server.fqdn or server.canonic_alias_fqdn,
                'status': 'online' if server.guest_power_state == 'poweredOn' else 'offline',
                'vcpu': server.vc_vm_vcpu or server.vcpu,
                'memory_gb': server.vc_vm_memory_gb or server.memory_gb,
                'disk_gb': server.vc_vm_disks_total_gb or server.mf_disks_total_gb,
                'vm_size': server.vc_vm_size or server.size,
                'cluster': server.vc_cluster,
                'vcf_domain': server.vcf_domain,
                'guest_os': server.guest_id,
                'power_state': server.guest_power_state,
                'tools_status': server.guest_tools_status,
                'created': server.vc_vm_creation_ts,
                'function': server.function,
                'env': server.env or server.cmdb_ci_env,
                'app_instance': server.app_instance,
                'tso_status': server.tso_status
            }
            env_dict['servers'].append(server_dict)
        
        environments_data.append(env_dict)
    
    # Staging Environment
    if stage_servers:
        env_dict = {
            'id': 'stage',
            'type': 'stage',
            'region': 'Staging',
            'servers': []
        }
        
        for server in stage_servers:
            server_dict = {
                'id': server.id,
                'name': server.name or server.canonic_alias or 'Unknown',
                'ip_address': server.ip_address or server.guest_ip_address,
                'fqdn': server.fqdn or server.canonic_alias_fqdn,
                'status': 'online' if server.guest_power_state == 'poweredOn' else 'offline',
                'vcpu': server.vc_vm_vcpu or server.vcpu,
                'memory_gb': server.vc_vm_memory_gb or server.memory_gb,
                'disk_gb': server.vc_vm_disks_total_gb or server.mf_disks_total_gb,
                'vm_size': server.vc_vm_size or server.size,
                'cluster': server.vc_cluster,
                'vcf_domain': server.vcf_domain,
                'guest_os': server.guest_id,
                'power_state': server.guest_power_state,
                'tools_status': server.guest_tools_status,
                'created': server.vc_vm_creation_ts,
                'function': server.function,
                'env': server.env or server.cmdb_ci_env,
                'app_instance': server.app_instance,
                'tso_status': server.tso_status
            }
            env_dict['servers'].append(server_dict)
        
        environments_data.append(env_dict)
    
    # Project info
    sample = prod_servers[0] if prod_servers else stage_servers[0] if stage_servers else None
    
    project_info = {
        'id': project_id,
        'name': project_id,
        'description': f'Infrastructure for {project_id}',
        'owner': sample.tso if sample and sample.tso else 'Unknown',
        'created_at': sample.import_timestamp if sample and sample.import_timestamp else datetime.utcnow()
    }
    
    return render_template('project_detail_lob.html',
                         project=project_info,
                         environments=environments_data)

# ========================================
# Updated capacity route in app.py
# ========================================

@app.route('/capacity')
def capacity():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    
    # Fetch ESXI cluster capacity data
    prod_clusters = CapacityDataProd.query.all()
    stage_clusters = CapacityDataStage.query.all()
    
    # Calculate summary statistics for Production
    prod_summary = {
        'total_clusters': len(prod_clusters),
        'total_cpu_cores': sum(c.cpu_usable_cores or 0 for c in prod_clusters),
        'avg_cpu_demand': round(sum(c.cpu_demand_percent or 0 for c in prod_clusters) / len(prod_clusters), 2) if prod_clusters else 0,
        'total_memory_capacity': round(sum(c.memory_usable_capacity or 0 for c in prod_clusters) / 1024, 2),  # Convert to TB
        'total_memory_consumed': round(sum(c.memory_consumed or 0 for c in prod_clusters) / 1024, 2),
        'total_disk_capacity': round(sum(c.disk_total_capacity or 0 for c in prod_clusters) / 1024, 2),  # Convert to TB
        'total_disk_provisioned': round(sum(c.disk_total_provisioned or 0 for c in prod_clusters) / 1024, 2),
        'avg_cpu_overcommit': round(sum(c.cpu_overcommit_ratio or 0 for c in prod_clusters) / len(prod_clusters), 2) if prod_clusters else 0,
        'avg_memory_overcommit': round(sum(c.memory_overcommit_ratio or 0 for c in prod_clusters) / len(prod_clusters), 2) if prod_clusters else 0,
    }
    
    # Calculate summary statistics for Stage
    stage_summary = {
        'total_clusters': len(stage_clusters),
        'total_cpu_cores': sum(c.cpu_usable_cores or 0 for c in stage_clusters),
        'avg_cpu_demand': round(sum(c.cpu_demand_percent or 0 for c in stage_clusters) / len(stage_clusters), 2) if stage_clusters else 0,
        'total_memory_capacity': round(sum(c.memory_usable_capacity or 0 for c in stage_clusters) / 1024, 2),
        'total_memory_consumed': round(sum(c.memory_consumed or 0 for c in stage_clusters) / 1024, 2),
        'total_disk_capacity': round(sum(c.disk_total_capacity or 0 for c in stage_clusters) / 1024, 2),
        'total_disk_provisioned': round(sum(c.disk_total_provisioned or 0 for c in stage_clusters) / 1024, 2),
        'avg_cpu_overcommit': round(sum(c.cpu_overcommit_ratio or 0 for c in stage_clusters) / len(stage_clusters), 2) if stage_clusters else 0,
        'avg_memory_overcommit': round(sum(c.memory_overcommit_ratio or 0 for c in stage_clusters) / len(stage_clusters), 2) if stage_clusters else 0,
    }
    
    return render_template('capacity.html',
                         prod_clusters=prod_clusters,
                         stage_clusters=stage_clusters,
                         prod_summary=prod_summary,
                         stage_summary=stage_summary)


# ========================================
# Helper function to format numbers
# ========================================

def format_bytes(bytes_value):
    """Convert bytes to human readable format"""
    if bytes_value is None:
        return "0 GB"
    
    # Assuming input is in GB
    if bytes_value >= 1024:
        return f"{bytes_value / 1024:.2f} TB"
    else:
        return f"{bytes_value:.2f} GB"


# Add this to your Jinja2 template filters
app.jinja_env.filters['format_bytes'] = format_bytes

# ==========================================
# ROUTES
# ==========================================

@app.route('/')
def login():
    if 'logged_in' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    
    user = User.query.filter_by(email=email).first()
    
    if user and check_password_hash(user.password, password):
        session['logged_in'] = True
        session['user_email'] = email
        session['user_id'] = user.id
        return redirect(url_for('dashboard'))
    
    flash('Invalid email or password', 'error')
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    
    # Fetch data from database
    servers = Server.query.all()
    total_servers = len(servers)
    active_projects = Project.query.count()
    active_alerts = Alert.query.count()
    
    # Calculate average CPU
    avg_cpu = db.session.query(db.func.avg(Server.cpu)).scalar() or 0
    
    return render_template('dashboard.html', 
                         servers=servers,
                         total_servers=total_servers,
                         active_projects=active_projects,
                         active_alerts=active_alerts,
                         avg_cpu=int(avg_cpu))




@app.route('/alerts')
def alerts():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    
    alerts = Alert.query.order_by(Alert.created_at.desc()).all()
    return render_template('alerts.html', alerts=alerts)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# ==========================================
# API ROUTES
# ==========================================

@app.route('/api/servers')
def api_servers():
    servers = Server.query.all()
    return {
        'servers': [{
            'id': s.id,
            'name': s.name,
            'status': s.status,
            'cpu': s.cpu,
            'memory': s.memory,
            'uptime': s.uptime
        } for s in servers]
    }

@app.route('/api/capacity')
def api_capacity():
    capacities = ServerCapacity.query.all()
    return {
        'capacities': [{
            'server_name': c.server.name,
            'total_storage': c.total_storage,
            'used_storage': c.used_storage,
            'storage_percentage': c.storage_percentage,
            'cpu_usage': c.cpu_usage,
            'ram_usage': c.ram_usage
        } for c in capacities]
    }

@app.route('/api/projects')
def api_projects():
    projects = Project.query.all()
    return {
        'projects': [{
            'id': p.id,
            'name': p.name,
            'owner': p.owner,
            'environments': len(p.environments)
        } for p in projects]
    }

# ==========================================
# DATABASE INITIALIZATION
# ==========================================

def seed_basic_data():
    """Seed basic server data for dashboard and capacity pages"""
    if Server.query.first() is not None:
        return
    
    # Create servers
    servers_data = [
        {'name': 'prod-web-01', 'status': 'online', 'cpu': 45, 'memory': 62, 'uptime': '23 days'},
        {'name': 'prod-db-01', 'status': 'online', 'cpu': 78, 'memory': 84, 'uptime': '45 days'},
        {'name': 'dev-api-02', 'status': 'warning', 'cpu': 91, 'memory': 88, 'uptime': '12 days'},
        {'name': 'staging-web-01', 'status': 'online', 'cpu': 34, 'memory': 56, 'uptime': '8 days'},
        {'name': 'prod-cache-01', 'status': 'online', 'cpu': 67, 'memory': 73, 'uptime': '30 days'},
    ]
    
    for data in servers_data:
        server = Server(**data)
        db.session.add(server)
    
    db.session.commit()
    
    # Create server capacities
    capacities_data = [
        {'server_id': 1, 'total_storage': '500 GB', 'used_storage': '345 GB', 'available_storage': '155 GB', 
         'storage_percentage': 69, 'cpu_cores': 8, 'cpu_usage': 45, 'total_ram': '32 GB', 'ram_usage': 62},
        {'server_id': 2, 'total_storage': '2 TB', 'used_storage': '1.8 TB', 'available_storage': '200 GB', 
         'storage_percentage': 90, 'cpu_cores': 16, 'cpu_usage': 78, 'total_ram': '64 GB', 'ram_usage': 84},
        {'server_id': 3, 'total_storage': '250 GB', 'used_storage': '89 GB', 'available_storage': '161 GB', 
         'storage_percentage': 36, 'cpu_cores': 4, 'cpu_usage': 91, 'total_ram': '16 GB', 'ram_usage': 88},
        {'server_id': 4, 'total_storage': '500 GB', 'used_storage': '198 GB', 'available_storage': '302 GB', 
         'storage_percentage': 40, 'cpu_cores': 8, 'cpu_usage': 34, 'total_ram': '32 GB', 'ram_usage': 56},
        {'server_id': 5, 'total_storage': '1 TB', 'used_storage': '756 GB', 'available_storage': '244 GB', 
         'storage_percentage': 76, 'cpu_cores': 12, 'cpu_usage': 67, 'total_ram': '48 GB', 'ram_usage': 73},
    ]
    
    for data in capacities_data:
        capacity = ServerCapacity(**data)
        db.session.add(capacity)
    
    # Create alerts
    alerts_data = [
        {'server_id': 3, 'alert_type': 'CPU', 'message': 'CPU usage exceeded 90%', 'severity': 'warning'},
        {'server_id': 2, 'alert_type': 'Storage', 'message': 'Disk space above 85%', 'severity': 'warning'},
        {'server_id': 5, 'alert_type': 'Memory', 'message': 'Memory usage critical', 'severity': 'offline'},
    ]
    
    for data in alerts_data:
        alert = Alert(**data)
        db.session.add(alert)
    
    db.session.commit()
    print("Basic server data seeded!")

def seed_project_data():
    """Seed enhanced project structure data"""
    if Project.query.first() is not None:
        return
    
    # Create Projects
    project1 = Project(
        name='E-Commerce Platform',
        description='Main customer-facing application',
        owner='John Doe'
    )
    project2 = Project(
        name='Analytics Dashboard',
        description='Real-time analytics and reporting',
        owner='Jane Smith'
    )
    project3 = Project(
        name='Mobile API',
        description='Backend API for mobile applications',
        owner='Bob Johnson'
    )
    
    db.session.add_all([project1, project2, project3])
    db.session.commit()
    
    # Create Environments for Project 1 (E-Commerce)
    env1_dev = ProjectEnvironment(project_id=project1.id, environment_type='dev', region='US-East')
    env1_stage = ProjectEnvironment(project_id=project1.id, environment_type='stage', region='US-West')
    env1_prod = ProjectEnvironment(project_id=project1.id, environment_type='prod', region='US-East')
    
    # Create Environments for Project 2 (Analytics)
    env2_dev = ProjectEnvironment(project_id=project2.id, environment_type='dev', region='EU-Central')
    env2_prod = ProjectEnvironment(project_id=project2.id, environment_type='prod', region='EU-West')
    
    # Create Environments for Project 3 (Mobile API)
    env3_dev = ProjectEnvironment(project_id=project3.id, environment_type='dev', region='Asia-Pacific')
    env3_stage = ProjectEnvironment(project_id=project3.id, environment_type='stage', region='Asia-Pacific')
    env3_prod = ProjectEnvironment(project_id=project3.id, environment_type='prod', region='US-West')
    
    db.session.add_all([env1_dev, env1_stage, env1_prod, env2_dev, env2_prod, env3_dev, env3_stage, env3_prod])
    db.session.commit()
    
    # Create Servers for Project 1 - Dev
    servers_p1_dev = [
        ServerNew(environment_id=env1_dev.id, name='dev-web-01', ip_address='192.168.1.10', os='Ubuntu 22.04',
                 status='online', cpu_cores=4, cpu_usage=35, ram='16 GB', ram_usage=45, storage='250 GB', storage_used=30, uptime='15 days'),
        ServerNew(environment_id=env1_dev.id, name='dev-db-01', ip_address='192.168.1.11', os='Ubuntu 22.04',
                 status='online', cpu_cores=8, cpu_usage=60, ram='32 GB', ram_usage=70, storage='500 GB', storage_used=55, uptime='15 days'),
    ]
    
    # Create Servers for Project 1 - Stage
    servers_p1_stage = [
        ServerNew(environment_id=env1_stage.id, name='stage-web-01', ip_address='192.168.2.10', os='Ubuntu 22.04',
                 status='online', cpu_cores=8, cpu_usage=45, ram='32 GB', ram_usage=55, storage='500 GB', storage_used=40, uptime='30 days'),
        ServerNew(environment_id=env1_stage.id, name='stage-db-01', ip_address='192.168.2.11', os='CentOS 8',
                 status='online', cpu_cores=16, cpu_usage=70, ram='64 GB', ram_usage=75, storage='1 TB', storage_used=65, uptime='30 days'),
    ]
    
    # Create Servers for Project 1 - Prod
    servers_p1_prod = [
        ServerNew(environment_id=env1_prod.id, name='prod-web-01', ip_address='10.0.1.10', os='Ubuntu 22.04',
                 status='online', cpu_cores=16, cpu_usage=55, ram='64 GB', ram_usage=65, storage='1 TB', storage_used=50, uptime='90 days'),
        ServerNew(environment_id=env1_prod.id, name='prod-db-01', ip_address='10.0.1.11', os='CentOS 8',
                 status='online', cpu_cores=32, cpu_usage=75, ram='128 GB', ram_usage=80, storage='2 TB', storage_used=70, uptime='90 days'),
        ServerNew(environment_id=env1_prod.id, name='prod-cache-01', ip_address='10.0.1.12', os='Ubuntu 22.04',
                 status='online', cpu_cores=8, cpu_usage=40, ram='32 GB', ram_usage=60, storage='500 GB', storage_used=35, uptime='90 days'),
    ]
    
    # Create Servers for Project 2
    servers_p2_dev = [
        ServerNew(environment_id=env2_dev.id, name='dev-analytics-01', ip_address='172.16.1.10', os='Ubuntu 20.04',
                 status='online', cpu_cores=8, cpu_usage=50, ram='32 GB', ram_usage=60, storage='1 TB', storage_used=45, uptime='20 days'),
    ]
    
    servers_p2_prod = [
        ServerNew(environment_id=env2_prod.id, name='prod-analytics-01', ip_address='10.1.1.10', os='Ubuntu 20.04',
                 status='online', cpu_cores=16, cpu_usage=65, ram='64 GB', ram_usage=75, storage='2 TB', storage_used=60, uptime='120 days'),
        ServerNew(environment_id=env2_prod.id, name='prod-analytics-db-01', ip_address='10.1.1.11', os='CentOS 8',
                 status='online', cpu_cores=24, cpu_usage=70, ram='96 GB', ram_usage=82, storage='3 TB', storage_used=75, uptime='120 days'),
    ]
    
    # Create Servers for Project 3
    servers_p3_dev = [
        ServerNew(environment_id=env3_dev.id, name='dev-api-01', ip_address='192.168.3.10', os='Ubuntu 22.04',
                 status='online', cpu_cores=4, cpu_usage=30, ram='16 GB', ram_usage=40, storage='250 GB', storage_used=25, uptime='10 days'),
    ]
    
    servers_p3_stage = [
        ServerNew(environment_id=env3_stage.id, name='stage-api-01', ip_address='192.168.4.10', os='Ubuntu 22.04',
                 status='online', cpu_cores=8, cpu_usage=40, ram='32 GB', ram_usage=50, storage='500 GB', storage_used=35, uptime='25 days'),
    ]
    
    servers_p3_prod = [
        ServerNew(environment_id=env3_prod.id, name='prod-api-01', ip_address='10.2.1.10', os='Ubuntu 22.04',
                 status='online', cpu_cores=12, cpu_usage=58, ram='48 GB', ram_usage=68, storage='1 TB', storage_used=52, uptime='60 days'),
        ServerNew(environment_id=env3_prod.id, name='prod-api-db-01', ip_address='10.2.1.11', os='PostgreSQL Server',
                 status='online', cpu_cores=16, cpu_usage=72, ram='64 GB', ram_usage=78, storage='2 TB', storage_used=68, uptime='60 days'),
    ]
    
    all_servers = servers_p1_dev + servers_p1_stage + servers_p1_prod + servers_p2_dev + servers_p2_prod + servers_p3_dev + servers_p3_stage + servers_p3_prod
    db.session.add_all(all_servers)
    db.session.commit()
    
    # Create Services
    services = [
        # Project 1 Dev
        ServiceNew(server_id=all_servers[0].id, name='Nginx', port='80, 443', status='online', response_time='25ms'),
        ServiceNew(server_id=all_servers[0].id, name='Node.js', port='3000', status='online', response_time='50ms'),
        ServiceNew(server_id=all_servers[1].id, name='PostgreSQL', port='5432', status='online', response_time='15ms'),
        
        # Project 1 Stage
        ServiceNew(server_id=all_servers[2].id, name='Nginx', port='80, 443', status='online', response_time='30ms'),
        ServiceNew(server_id=all_servers[2].id, name='Node.js', port='3000', status='online', response_time='55ms'),
        ServiceNew(server_id=all_servers[3].id, name='PostgreSQL', port='5432', status='online', response_time='20ms'),
        
        # Project 1 Prod
        ServiceNew(server_id=all_servers[4].id, name='Nginx', port='80, 443', status='online', response_time='35ms'),
        ServiceNew(server_id=all_servers[4].id, name='Node.js', port='3000', status='online', response_time='45ms'),
        ServiceNew(server_id=all_servers[5].id, name='PostgreSQL', port='5432', status='online', response_time='18ms'),
        ServiceNew(server_id=all_servers[6].id, name='Redis', port='6379', status='online', response_time='8ms'),
        
        # Project 2 Dev
        ServiceNew(server_id=all_servers[7].id, name='Python API', port='5000', status='online', response_time='60ms'),
        ServiceNew(server_id=all_servers[7].id, name='Elasticsearch', port='9200', status='online', response_time='100ms'),
        
        # Project 2 Prod
        ServiceNew(server_id=all_servers[8].id, name='Python API', port='5000', status='online', response_time='55ms'),
        ServiceNew(server_id=all_servers[8].id, name='Elasticsearch', port='9200', status='online', response_time='85ms'),
        ServiceNew(server_id=all_servers[9].id, name='PostgreSQL', port='5432', status='online', response_time='22ms'),
        ServiceNew(server_id=all_servers[9].id, name='MongoDB', port='27017', status='online', response_time='28ms'),
        
        # Project 3 Dev
        ServiceNew(server_id=all_servers[10].id, name='Express API', port='4000', status='online', response_time='40ms'),
        ServiceNew(server_id=all_servers[10].id, name='GraphQL', port='4000/graphql', status='online', response_time='65ms'),
        
        # Project 3 Stage
        ServiceNew(server_id=all_servers[11].id, name='Express API', port='4000', status='online', response_time='42ms'),
        ServiceNew(server_id=all_servers[11].id, name='GraphQL', port='4000/graphql', status='online', response_time='62ms'),
        
        # Project 3 Prod
        ServiceNew(server_id=all_servers[12].id, name='Express API', port='4000', status='online', response_time='38ms'),
        ServiceNew(server_id=all_servers[12].id, name='GraphQL', port='4000/graphql', status='online', response_time='58ms'),
        ServiceNew(server_id=all_servers[13].id, name='PostgreSQL', port='5432', status='online', response_time='16ms'),
    ]
    
    db.session.add_all(services)
    db.session.commit()
    
    print("Project data seeded successfully!")

def init_db():
    """Initialize database and seed data"""
    with app.app_context():
        db.create_all()
        
        # Create default user
        if User.query.first() is None:
            user = User(
                email='admin@dotsh.com',
                password=generate_password_hash('admin123')
            )
            db.session.add(user)
            db.session.commit()
            print("Default user created!")
        
        # Seed basic server data
        seed_basic_data()
        
        # Seed project data
        seed_project_data()
        
        print("\n" + "="*50)
        print("Database initialized successfully!")
        print("="*50)
        print("Default Login Credentials:")
        print("  Email: admin@dotsh.com")
        print("  Password: admin123")
        print("="*50 + "\n")

# ==========================================
# MAIN
# ==========================================

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)