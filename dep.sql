-- SQL Script to Create app_dependency Table
-- Run this script in your PostgreSQL database

-- Create the app_dependency table
CREATE TABLE IF NOT EXISTS app_dependency (
    id SERIAL PRIMARY KEY,
    source_ciid VARCHAR(255),
    upstream_ciid VARCHAR(255),
    down_stream_ciid VARCHAR(255),
    connection_type VARCHAR(255)
);

-- Create indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_app_dependency_source_ciid ON app_dependency(source_ciid);
CREATE INDEX IF NOT EXISTS idx_app_dependency_upstream_ciid ON app_dependency(upstream_ciid);
CREATE INDEX IF NOT EXISTS idx_app_dependency_downstream_ciid ON app_dependency(down_stream_ciid);

-- Optional: Add sample data for testing
-- Uncomment the lines below to insert test data

/*
INSERT INTO app_dependency (source_ciid, upstream_ciid, down_stream_ciid, connection_type) VALUES
('12345', '12340', NULL, 'API'),
('12345', '12341', NULL, 'Database'),
('12345', '12342', NULL, 'Message Queue'),
('12346', '12345', NULL, 'REST API'),
('12347', '12345', NULL, 'WebSocket'),
('12345', NULL, '12348', 'Event Stream');
*/

-- Verify the table was created
SELECT table_name, column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'app_dependency'
ORDER BY ordinal_position;

-- Check row count
SELECT COUNT(*) as total_dependencies FROM app_dependency;

COMMENT ON TABLE app_dependency IS 'Stores application dependencies between ITAM CIIDs';
COMMENT ON COLUMN app_dependency.source_ciid IS 'The ITAM CIID that has dependencies';
COMMENT ON COLUMN app_dependency.upstream_ciid IS 'The ITAM CIID that this application depends on (upstream)';
COMMENT ON COLUMN app_dependency.down_stream_ciid IS 'The ITAM CIID that depends on this application (downstream)';
COMMENT ON COLUMN app_dependency.connection_type IS 'Type of connection (e.g., API, Database, Message Queue, etc.)';