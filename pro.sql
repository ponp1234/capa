-- Table: public.lob_inventory1

-- DROP TABLE IF EXISTS public.lob_inventory1;

CREATE TABLE IF NOT EXISTS public.lob_inventory1
(
    id integer NOT NULL DEFAULT nextval('lob_inventory1_id_seq'::regclass),
    lob character varying COLLATE pg_catalog."default",
    ito_unit character varying COLLATE pg_catalog."default",
    itam_ciid character varying COLLATE pg_catalog."default",
    app_instance character varying COLLATE pg_catalog."default",
    tso character varying COLLATE pg_catalog."default",
    tso_status character varying COLLATE pg_catalog."default",
    compute_config text COLLATE pg_catalog."default",
    canonic_alias character varying COLLATE pg_catalog."default",
    name character varying COLLATE pg_catalog."default",
    ip_address character varying COLLATE pg_catalog."default",
    infra character varying COLLATE pg_catalog."default",
    cidr character varying COLLATE pg_catalog."default",
    function character varying COLLATE pg_catalog."default",
    warn_orphan character varying COLLATE pg_catalog."default",
    decomm_after timestamp without time zone,
    decomm_source character varying COLLATE pg_catalog."default",
    decomm_comment character varying COLLATE pg_catalog."default",
    vc_vm_poweredoff_at_or_before timestamp without time zone,
    type character varying COLLATE pg_catalog."default",
    size character varying COLLATE pg_catalog."default",
    vcpu integer,
    memory_gb integer,
    warn_vm_size character varying COLLATE pg_catalog."default",
    product_mf character varying COLLATE pg_catalog."default",
    vm_image character varying COLLATE pg_catalog."default",
    error_vm_image character varying COLLATE pg_catalog."default",
    canonic_alias_fqdn character varying COLLATE pg_catalog."default",
    fqdn character varying COLLATE pg_catalog."default",
    infoblox_network_infra character varying COLLATE pg_catalog."default",
    config_canonic_id character varying COLLATE pg_catalog."default",
    serial_number character varying COLLATE pg_catalog."default",
    cmdb_ci_sat_signoff character varying COLLATE pg_catalog."default",
    cmdb_ci_env character varying COLLATE pg_catalog."default",
    cmdb_ci_op_status character varying COLLATE pg_catalog."default",
    warn_vm_shipped_folder character varying COLLATE pg_catalog."default",
    vc_vm_folder_full character varying COLLATE pg_catalog."default",
    vcf_domain character varying COLLATE pg_catalog."default",
    vc_cluster character varying COLLATE pg_catalog."default",
    vc_cluster_function character varying COLLATE pg_catalog."default",
    vc_vm_creation_ts timestamp without time zone,
    mf_disks_total_gb integer,
    vc_vm_disks_total_gb integer,
    mf_disks character varying COLLATE pg_catalog."default",
    vc_vm_disks character varying COLLATE pg_catalog."default",
    vc_vm_size character varying COLLATE pg_catalog."default",
    vc_vm_vcpu integer,
    vc_vm_memory_gb integer,
    vc_vm_reservations character varying COLLATE pg_catalog."default",
    env character varying COLLATE pg_catalog."default",
    vip_host_name character varying COLLATE pg_catalog."default",
    vip_host_ref character varying COLLATE pg_catalog."default",
    vip_host_infra character varying COLLATE pg_catalog."default",
    lb_cname_name character varying COLLATE pg_catalog."default",
    lb_cname_ref character varying COLLATE pg_catalog."default",
    vc_vm_annotation text COLLATE pg_catalog."default",
    guest_collect_ts timestamp without time zone,
    guest_ip_address character varying COLLATE pg_catalog."default",
    guest_power_state character varying COLLATE pg_catalog."default",
    guest_id character varying COLLATE pg_catalog."default",
    guest_tools_running_status character varying COLLATE pg_catalog."default",
    guest_tools_status character varying COLLATE pg_catalog."default",
    vc_cluster_az character varying COLLATE pg_catalog."default",
    vc_vm_instance_uuid character varying COLLATE pg_catalog."default",
    vc_vm_id character varying COLLATE pg_catalog."default",
    cmdb_ci_sys_id character varying COLLATE pg_catalog."default",
    cmdb_ci_first_discovered timestamp without time zone,
    cmdb_ci_last_discovered timestamp without time zone,
    infoblox_ref character varying COLLATE pg_catalog."default",
    infoblox_network_ref character varying COLLATE pg_catalog."default",
    mac_address character varying COLLATE pg_catalog."default",
    host_record_name character varying COLLATE pg_catalog."default",
    error_image_os character varying COLLATE pg_catalog."default",
    import_timestamp timestamp without time zone,
    state character varying COLLATE pg_catalog."default",
    CONSTRAINT lob_inventory1_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.lob_inventory1
    OWNER to postgres;


    -- Table: public.lob_inventory1_stage

-- DROP TABLE IF EXISTS public.lob_inventory1_stage;

CREATE TABLE IF NOT EXISTS public.lob_inventory1_stage
(
    id integer NOT NULL DEFAULT nextval('lob_inventory1_stage_id_seq'::regclass),
    lob character varying COLLATE pg_catalog."default",
    ito_unit character varying COLLATE pg_catalog."default",
    itam_ciid character varying COLLATE pg_catalog."default",
    app_instance character varying COLLATE pg_catalog."default",
    tso character varying COLLATE pg_catalog."default",
    tso_status character varying COLLATE pg_catalog."default",
    compute_config text COLLATE pg_catalog."default",
    canonic_alias character varying COLLATE pg_catalog."default",
    name character varying COLLATE pg_catalog."default",
    ip_address character varying COLLATE pg_catalog."default",
    infra character varying COLLATE pg_catalog."default",
    cidr character varying COLLATE pg_catalog."default",
    function character varying COLLATE pg_catalog."default",
    warn_orphan character varying COLLATE pg_catalog."default",
    decomm_after timestamp without time zone,
    decomm_source character varying COLLATE pg_catalog."default",
    decomm_comment character varying COLLATE pg_catalog."default",
    vc_vm_poweredoff_at_or_before timestamp without time zone,
    type character varying COLLATE pg_catalog."default",
    size character varying COLLATE pg_catalog."default",
    vcpu integer,
    memory_gb integer,
    warn_vm_size character varying COLLATE pg_catalog."default",
    product_mf character varying COLLATE pg_catalog."default",
    vm_image character varying COLLATE pg_catalog."default",
    error_vm_image character varying COLLATE pg_catalog."default",
    canonic_alias_fqdn character varying COLLATE pg_catalog."default",
    fqdn character varying COLLATE pg_catalog."default",
    infoblox_network_infra character varying COLLATE pg_catalog."default",
    config_canonic_id character varying COLLATE pg_catalog."default",
    serial_number character varying COLLATE pg_catalog."default",
    cmdb_ci_sat_signoff character varying COLLATE pg_catalog."default",
    cmdb_ci_env character varying COLLATE pg_catalog."default",
    cmdb_ci_op_status character varying COLLATE pg_catalog."default",
    warn_vm_shipped_folder character varying COLLATE pg_catalog."default",
    vc_vm_folder_full character varying COLLATE pg_catalog."default",
    vcf_domain character varying COLLATE pg_catalog."default",
    vc_cluster character varying COLLATE pg_catalog."default",
    vc_cluster_function character varying COLLATE pg_catalog."default",
    vc_vm_creation_ts timestamp without time zone,
    mf_disks_total_gb integer,
    vc_vm_disks_total_gb integer,
    mf_disks character varying COLLATE pg_catalog."default",
    vc_vm_disks character varying COLLATE pg_catalog."default",
    vc_vm_size character varying COLLATE pg_catalog."default",
    vc_vm_vcpu integer,
    vc_vm_memory_gb integer,
    vc_vm_reservations character varying COLLATE pg_catalog."default",
    env character varying COLLATE pg_catalog."default",
    vip_host_name character varying COLLATE pg_catalog."default",
    vip_host_ref character varying COLLATE pg_catalog."default",
    vip_host_infra character varying COLLATE pg_catalog."default",
    lb_cname_name character varying COLLATE pg_catalog."default",
    lb_cname_ref character varying COLLATE pg_catalog."default",
    vc_vm_annotation text COLLATE pg_catalog."default",
    guest_collect_ts timestamp without time zone,
    guest_ip_address character varying COLLATE pg_catalog."default",
    guest_power_state character varying COLLATE pg_catalog."default",
    guest_id character varying COLLATE pg_catalog."default",
    guest_tools_running_status character varying COLLATE pg_catalog."default",
    guest_tools_status character varying COLLATE pg_catalog."default",
    vc_cluster_az character varying COLLATE pg_catalog."default",
    vc_vm_instance_uuid character varying COLLATE pg_catalog."default",
    vc_vm_id character varying COLLATE pg_catalog."default",
    cmdb_ci_sys_id character varying COLLATE pg_catalog."default",
    cmdb_ci_first_discovered timestamp without time zone,
    cmdb_ci_last_discovered timestamp without time zone,
    infoblox_ref character varying COLLATE pg_catalog."default",
    infoblox_network_ref character varying COLLATE pg_catalog."default",
    mac_address character varying COLLATE pg_catalog."default",
    host_record_name character varying COLLATE pg_catalog."default",
    error_image_os character varying COLLATE pg_catalog."default",
    import_timestamp timestamp without time zone,
    state character varying COLLATE pg_catalog."default",
    CONSTRAINT lob_inventory1_stage_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.lob_inventory1_stage
    OWNER to postgres;

-- ========================================
-- SAMPLE DATA FOR LOB INVENTORY TABLES
-- Ready to use SQL INSERT statements
-- ========================================

-- Clear existing data (optional)
-- DELETE FROM public.lob_inventory1_stage;
-- DELETE FROM public.lob_inventory1;

-- ========================================
-- PRODUCTION ENVIRONMENT DATA (lob_inventory1)
-- ========================================

-- Finance LOB - Production Servers
INSERT INTO public.lob_inventory1 (lob, ito_unit, itam_ciid, app_instance, tso, tso_status, canonic_alias, name, ip_address, infra, function, type, size, vcpu, memory_gb, fqdn, vc_cluster, vcf_domain, vc_vm_creation_ts, vc_vm_disks_total_gb, vc_vm_size, vc_vm_vcpu, vc_vm_memory_gb, env, guest_ip_address, guest_power_state, guest_id, guest_tools_status, import_timestamp, state)
VALUES 
('Finance', 'ITO-East', 'CIID-45231', 'Finance-APP-1', 'John Smith', 'Active', 'finance-prod-001', 'finance-prod-001', '10.10.10.101', 'vSphere', 'Web Server', 'VM', 'Large', 8, 32, 'finance-prod-001.company.com', 'Cluster-Prod-01', 'Domain-Production', '2024-06-15 10:30:00', 500, 'Large', 8, 32, 'production', '10.10.10.101', 'poweredOn', 'rhel8', 'guestToolsRunning', NOW(), 'active'),

('Finance', 'ITO-East', 'CIID-45232', 'Finance-APP-2', 'John Smith', 'Active', 'finance-prod-002', 'finance-prod-002', '10.10.10.102', 'vSphere', 'Database', 'VM', 'X-Large', 16, 64, 'finance-prod-002.company.com', 'Cluster-Prod-01', 'Domain-Production', '2024-06-15 11:00:00', 1000, 'X-Large', 16, 64, 'production', '10.10.10.102', 'poweredOn', 'rhel8', 'guestToolsRunning', NOW(), 'active'),

('Finance', 'ITO-East', 'CIID-45233', 'Finance-APP-3', 'John Smith', 'Active', 'finance-prod-003', 'finance-prod-003', '10.10.10.103', 'vSphere', 'Application', 'VM', 'Medium', 4, 16, 'finance-prod-003.company.com', 'Cluster-Prod-02', 'Domain-Production', '2024-07-20 09:15:00', 250, 'Medium', 4, 16, 'production', '10.10.10.103', 'poweredOn', 'rhel7', 'guestToolsRunning', NOW(), 'active'),

('Finance', 'ITO-West', 'CIID-45234', 'Finance-APP-4', 'Jane Doe', 'Active', 'finance-prod-004', 'finance-prod-004', '10.10.10.104', 'AWS', 'Load Balancer', 'VM', 'Medium', 4, 16, 'finance-prod-004.company.com', 'Cluster-Prod-01', 'Domain-Production', '2024-08-10 14:20:00', 100, 'Medium', 4, 16, 'production', '10.10.10.104', 'poweredOn', 'ubuntu20.04', 'guestToolsRunning', NOW(), 'active'),

('Finance', 'ITO-West', 'CIID-45235', 'Finance-APP-5', 'Jane Doe', 'Active', 'finance-prod-005', 'finance-prod-005', '10.10.10.105', 'vSphere', 'Cache', 'VM', 'Small', 2, 8, 'finance-prod-005.company.com', 'Cluster-Prod-02', 'Domain-Production', '2024-09-05 16:45:00', 100, 'Small', 2, 8, 'production', '10.10.10.105', 'poweredOff', 'rhel8', 'guestToolsNotRunning', NOW(), 'active');

-- HR LOB - Production Servers
INSERT INTO public.lob_inventory1 (lob, ito_unit, itam_ciid, app_instance, tso, tso_status, canonic_alias, name, ip_address, infra, function, type, size, vcpu, memory_gb, fqdn, vc_cluster, vcf_domain, vc_vm_creation_ts, vc_vm_disks_total_gb, vc_vm_size, vc_vm_vcpu, vc_vm_memory_gb, env, guest_ip_address, guest_power_state, guest_id, guest_tools_status, import_timestamp, state)
VALUES 
('HR', 'ITO-Central', 'CIID-56721', 'HR-APP-1', 'Bob Wilson', 'Active', 'hr-prod-001', 'hr-prod-001', '10.20.10.101', 'Azure', 'Web Server', 'VM', 'Medium', 4, 16, 'hr-prod-001.company.com', 'Cluster-Prod-01', 'Domain-Production', '2024-05-12 08:00:00', 250, 'Medium', 4, 16, 'production', '10.20.10.101', 'poweredOn', 'windows2019', 'guestToolsRunning', NOW(), 'active'),

('HR', 'ITO-Central', 'CIID-56722', 'HR-APP-2', 'Bob Wilson', 'Active', 'hr-prod-002', 'hr-prod-002', '10.20.10.102', 'Azure', 'Database', 'VM', 'Large', 8, 32, 'hr-prod-002.company.com', 'Cluster-Prod-01', 'Domain-Production', '2024-05-12 08:30:00', 500, 'Large', 8, 32, 'production', '10.20.10.102', 'poweredOn', 'windows2019', 'guestToolsRunning', NOW(), 'active'),

('HR', 'ITO-Central', 'CIID-56723', 'HR-APP-3', 'Alice Johnson', 'Active', 'hr-prod-003', 'hr-prod-003', '10.20.10.103', 'vSphere', 'Application', 'VM', 'Medium', 4, 16, 'hr-prod-003.company.com', 'Cluster-Prod-02', 'Domain-Production', '2024-06-18 10:15:00', 250, 'Medium', 4, 16, 'production', '10.20.10.103', 'poweredOn', 'rhel8', 'guestToolsRunning', NOW(), 'active');

-- Marketing LOB - Production Servers
INSERT INTO public.lob_inventory1 (lob, ito_unit, itam_ciid, app_instance, tso, tso_status, canonic_alias, name, ip_address, infra, function, type, size, vcpu, memory_gb, fqdn, vc_cluster, vcf_domain, vc_vm_creation_ts, vc_vm_disks_total_gb, vc_vm_size, vc_vm_vcpu, vc_vm_memory_gb, env, guest_ip_address, guest_power_state, guest_id, guest_tools_status, import_timestamp, state)
VALUES 
('Marketing', 'ITO-Cloud', 'CIID-78901', 'Marketing-APP-1', 'Mike Davis', 'Active', 'marketing-prod-001', 'marketing-prod-001', '10.30.10.101', 'AWS', 'Web Server', 'VM', 'Large', 8, 32, 'marketing-prod-001.company.com', 'Cluster-Prod-01', 'Domain-Production', '2024-07-01 09:00:00', 500, 'Large', 8, 32, 'production', '10.30.10.101', 'poweredOn', 'ubuntu20.04', 'guestToolsRunning', NOW(), 'active'),

('Marketing', 'ITO-Cloud', 'CIID-78902', 'Marketing-APP-2', 'Mike Davis', 'Active', 'marketing-prod-002', 'marketing-prod-002', '10.30.10.102', 'AWS', 'Database', 'VM', 'X-Large', 16, 64, 'marketing-prod-002.company.com', 'Cluster-Prod-01', 'Domain-Production', '2024-07-01 09:30:00', 1000, 'X-Large', 16, 64, 'production', '10.30.10.102', 'poweredOn', 'ubuntu20.04', 'guestToolsRunning', NOW(), 'active'),

('Marketing', 'ITO-Cloud', 'CIID-78903', 'Marketing-APP-3', 'John Smith', 'Active', 'marketing-prod-003', 'marketing-prod-003', '10.30.10.103', 'vSphere', 'Cache', 'VM', 'Medium', 4, 16, 'marketing-prod-003.company.com', 'Cluster-Prod-02', 'Domain-Production', '2024-08-15 11:00:00', 250, 'Medium', 4, 16, 'production', '10.30.10.103', 'poweredOn', 'rhel8', 'guestToolsRunning', NOW(), 'active'),

('Marketing', 'ITO-Cloud', 'CIID-78904', 'Marketing-APP-4', 'John Smith', 'Active', 'marketing-prod-004', 'marketing-prod-004', '10.30.10.104', 'vSphere', 'Application', 'VM', 'Large', 8, 32, 'marketing-prod-004.company.com', 'Cluster-Prod-01', 'Domain-Production', '2024-08-20 13:30:00', 500, 'Large', 8, 32, 'production', '10.30.10.104', 'poweredOff', 'rhel7', 'guestToolsNotRunning', NOW(), 'active');

-- Operations LOB - Production Servers
INSERT INTO public.lob_inventory1 (lob, ito_unit, itam_ciid, app_instance, tso, tso_status, canonic_alias, name, ip_address, infra, function, type, size, vcpu, memory_gb, fqdn, vc_cluster, vcf_domain, vc_vm_creation_ts, vc_vm_disks_total_gb, vc_vm_size, vc_vm_vcpu, vc_vm_memory_gb, env, guest_ip_address, guest_power_state, guest_id, guest_tools_status, import_timestamp, state)
VALUES 
('Operations', 'ITO-East', 'CIID-34512', 'Operations-APP-1', 'Jane Doe', 'Active', 'operations-prod-001', 'operations-prod-001', '10.40.10.101', 'On-Prem', 'Web Server', 'VM', 'Medium', 4, 16, 'operations-prod-001.company.com', 'Cluster-Prod-01', 'Domain-Production', '2024-04-10 07:00:00', 250, 'Medium', 4, 16, 'production', '10.40.10.101', 'poweredOn', 'centos7', 'guestToolsRunning', NOW(), 'active'),

('Operations', 'ITO-East', 'CIID-34513', 'Operations-APP-2', 'Jane Doe', 'Active', 'operations-prod-002', 'operations-prod-002', '10.40.10.102', 'On-Prem', 'Database', 'VM', 'Large', 8, 32, 'operations-prod-002.company.com', 'Cluster-Prod-02', 'Domain-Production', '2024-04-10 07:30:00', 500, 'Large', 8, 32, 'production', '10.40.10.102', 'poweredOn', 'rhel8', 'guestToolsRunning', NOW(), 'active'),

('Operations', 'ITO-West', 'CIID-34514', 'Operations-APP-3', 'Bob Wilson', 'Active', 'operations-prod-003', 'operations-prod-003', '10.40.10.103', 'vSphere', 'Application', 'VM', 'Medium', 4, 16, 'operations-prod-003.company.com', 'Cluster-Prod-01', 'Domain-Production', '2024-05-22 12:00:00', 250, 'Medium', 4, 16, 'production', '10.40.10.103', 'poweredOn', 'rhel8', 'guestToolsRunning', NOW(), 'active');

-- IT-Infrastructure LOB - Production Servers
INSERT INTO public.lob_inventory1 (lob, ito_unit, itam_ciid, app_instance, tso, tso_status, canonic_alias, name, ip_address, infra, function, type, size, vcpu, memory_gb, fqdn, vc_cluster, vcf_domain, vc_vm_creation_ts, vc_vm_disks_total_gb, vc_vm_size, vc_vm_vcpu, vc_vm_memory_gb, env, guest_ip_address, guest_power_state, guest_id, guest_tools_status, import_timestamp, state)
VALUES 
('IT-Infrastructure', 'ITO-Central', 'CIID-91234', 'IT-APP-1', 'Alice Johnson', 'Active', 'it-prod-001', 'it-prod-001', '10.50.10.101', 'vSphere', 'Load Balancer', 'VM', 'Large', 8, 32, 'it-prod-001.company.com', 'Cluster-Prod-01', 'Domain-Production', '2024-03-15 06:00:00', 500, 'Large', 8, 32, 'production', '10.50.10.101', 'poweredOn', 'rhel8', 'guestToolsRunning', NOW(), 'active'),

('IT-Infrastructure', 'ITO-Central', 'CIID-91235', 'IT-APP-2', 'Alice Johnson', 'Active', 'it-prod-002', 'it-prod-002', '10.50.10.102', 'vSphere', 'Web Server', 'VM', 'X-Large', 16, 64, 'it-prod-002.company.com', 'Cluster-Prod-02', 'Domain-Production', '2024-03-15 06:30:00', 1000, 'X-Large', 16, 64, 'production', '10.50.10.102', 'poweredOn', 'rhel8', 'guestToolsRunning', NOW(), 'active'),

('IT-Infrastructure', 'ITO-Central', 'CIID-91236', 'IT-APP-3', 'Mike Davis', 'Active', 'it-prod-003', 'it-prod-003', '10.50.10.103', 'vSphere', 'Database', 'VM', 'X-Large', 16, 64, 'it-prod-003.company.com', 'Cluster-Prod-01', 'Domain-Production', '2024-04-01 08:00:00', 1000, 'X-Large', 16, 64, 'production', '10.50.10.103', 'poweredOn', 'rhel8', 'guestToolsRunning', NOW(), 'active');


-- ========================================
-- STAGING ENVIRONMENT DATA (lob_inventory1_stage)
-- ========================================

-- Finance LOB - Staging Servers
INSERT INTO public.lob_inventory1_stage (lob, ito_unit, itam_ciid, app_instance, tso, tso_status, canonic_alias, name, ip_address, infra, function, type, size, vcpu, memory_gb, fqdn, vc_cluster, vcf_domain, vc_vm_creation_ts, vc_vm_disks_total_gb, vc_vm_size, vc_vm_vcpu, vc_vm_memory_gb, env, guest_ip_address, guest_power_state, guest_id, guest_tools_status, import_timestamp, state)
VALUES 
('Finance', 'ITO-East', 'CIID-45301', 'Finance-APP-1', 'John Smith', 'Active', 'finance-stage-001', 'finance-stage-001', '192.168.10.101', 'vSphere', 'Web Server', 'VM', 'Medium', 4, 16, 'finance-stage-001.stage.company.com', 'Cluster-Stage-01', 'Domain-Staging', '2024-07-01 10:00:00', 250, 'Medium', 4, 16, 'staging', '192.168.10.101', 'poweredOn', 'rhel8', 'guestToolsRunning', NOW(), 'active'),

('Finance', 'ITO-East', 'CIID-45302', 'Finance-APP-2', 'John Smith', 'Active', 'finance-stage-002', 'finance-stage-002', '192.168.10.102', 'vSphere', 'Database', 'VM', 'Large', 8, 32, 'finance-stage-002.stage.company.com', 'Cluster-Stage-01', 'Domain-Staging', '2024-07-01 10:30:00', 500, 'Large', 8, 32, 'staging', '192.168.10.102', 'poweredOn', 'rhel8', 'guestToolsRunning', NOW(), 'active'),

('Finance', 'ITO-West', 'CIID-45303', 'Finance-APP-3', 'Jane Doe', 'Active', 'finance-stage-003', 'finance-stage-003', '192.168.10.103', 'vSphere', 'Application', 'VM', 'Small', 2, 8, 'finance-stage-003.stage.company.com', 'Cluster-Stage-01', 'Domain-Staging', '2024-08-15 11:00:00', 100, 'Small', 2, 8, 'staging', '192.168.10.103', 'poweredOff', 'rhel7', 'guestToolsNotRunning', NOW(), 'active');

-- HR LOB - Staging Servers
INSERT INTO public.lob_inventory1_stage (lob, ito_unit, itam_ciid, app_instance, tso, tso_status, canonic_alias, name, ip_address, infra, function, type, size, vcpu, memory_gb, fqdn, vc_cluster, vcf_domain, vc_vm_creation_ts, vc_vm_disks_total_gb, vc_vm_size, vc_vm_vcpu, vc_vm_memory_gb, env, guest_ip_address, guest_power_state, guest_id, guest_tools_status, import_timestamp, state)
VALUES 
('HR', 'ITO-Central', 'CIID-56801', 'HR-APP-1', 'Bob Wilson', 'Active', 'hr-stage-001', 'hr-stage-001', '192.168.20.101', 'Azure', 'Web Server', 'VM', 'Small', 2, 8, 'hr-stage-001.stage.company.com', 'Cluster-Stage-01', 'Domain-Staging', '2024-06-01 09:00:00', 100, 'Small', 2, 8, 'staging', '192.168.20.101', 'poweredOn', 'windows2019', 'guestToolsRunning', NOW(), 'active'),

('HR', 'ITO-Central', 'CIID-56802', 'HR-APP-2', 'Bob Wilson', 'Active', 'hr-stage-002', 'hr-stage-002', '192.168.20.102', 'Azure', 'Database', 'VM', 'Medium', 4, 16, 'hr-stage-002.stage.company.com', 'Cluster-Stage-01', 'Domain-Staging', '2024-06-01 09:30:00', 250, 'Medium', 4, 16, 'staging', '192.168.20.102', 'poweredOn', 'windows2019', 'guestToolsRunning', NOW(), 'active');

-- Marketing LOB - Staging Servers
INSERT INTO public.lob_inventory1_stage (lob, ito_unit, itam_ciid, app_instance, tso, tso_status, canonic_alias, name, ip_address, infra, function, type, size, vcpu, memory_gb, fqdn, vc_cluster, vcf_domain, vc_vm_creation_ts, vc_vm_disks_total_gb, vc_vm_size, vc_vm_vcpu, vc_vm_memory_gb, env, guest_ip_address, guest_power_state, guest_id, guest_tools_status, import_timestamp, state)
VALUES 
('Marketing', 'ITO-Cloud', 'CIID-79001', 'Marketing-APP-1', 'Mike Davis', 'Active', 'marketing-stage-001', 'marketing-stage-001', '192.168.30.101', 'AWS', 'Web Server', 'VM', 'Medium', 4, 16, 'marketing-stage-001.stage.company.com', 'Cluster-Stage-01', 'Domain-Staging', '2024-07-15 10:00:00', 250, 'Medium', 4, 16, 'staging', '192.168.30.101', 'poweredOn', 'ubuntu20.04', 'guestToolsRunning', NOW(), 'active'),

('Marketing', 'ITO-Cloud', 'CIID-79002', 'Marketing-APP-2', 'Mike Davis', 'Active', 'marketing-stage-002', 'marketing-stage-002', '192.168.30.102', 'AWS', 'Database', 'VM', 'Large', 8, 32, 'marketing-stage-002.stage.company.com', 'Cluster-Stage-01', 'Domain-Staging', '2024-07-15 10:30:00', 500, 'Large', 8, 32, 'staging', '192.168.30.102', 'poweredOn', 'ubuntu20.04', 'guestToolsRunning', NOW(), 'active'),

('Marketing', 'ITO-Cloud', 'CIID-79003', 'Marketing-APP-3', 'John Smith', 'Active', 'marketing-stage-003', 'marketing-stage-003', '192.168.30.103', 'vSphere', 'Cache', 'VM', 'Small', 2, 8, 'marketing-stage-003.stage.company.com', 'Cluster-Stage-01', 'Domain-Staging', '2024-08-25 11:30:00', 100, 'Small', 2, 8, 'staging', '192.168.30.103', 'poweredOff', 'rhel8', 'guestToolsNotRunning', NOW(), 'active');

-- Operations LOB - Staging Servers
INSERT INTO public.lob_inventory1_stage (lob, ito_unit, itam_ciid, app_instance, tso, tso_status, canonic_alias, name, ip_address, infra, function, type, size, vcpu, memory_gb, fqdn, vc_cluster, vcf_domain, vc_vm_creation_ts, vc_vm_disks_total_gb, vc_vm_size, vc_vm_vcpu, vc_vm_memory_gb, env, guest_ip_address, guest_power_state, guest_id, guest_tools_status, import_timestamp, state)
VALUES 
('Operations', 'ITO-East', 'CIID-34601', 'Operations-APP-1', 'Jane Doe', 'Active', 'operations-stage-001', 'operations-stage-001', '192.168.40.101', 'On-Prem', 'Web Server', 'VM', 'Small', 2, 8, 'operations-stage-001.stage.company.com', 'Cluster-Stage-01', 'Domain-Staging', '2024-05-01 08:00:00', 100, 'Small', 2, 8, 'staging', '192.168.40.101', 'poweredOn', 'centos7', 'guestToolsRunning', NOW(), 'active'),

('Operations', 'ITO-East', 'CIID-34602', 'Operations-APP-2', 'Jane Doe', 'Active', 'operations-stage-002', 'operations-stage-002', '192.168.40.102', 'On-Prem', 'Database', 'VM', 'Medium', 4, 16, 'operations-stage-002.stage.company.com', 'Cluster-Stage-01', 'Domain-Staging', '2024-05-01 08:30:00', 250, 'Medium', 4, 16, 'staging', '192.168.40.102', 'poweredOn', 'rhel8', 'guestToolsRunning', NOW(), 'active');

-- IT-Infrastructure LOB - Staging Servers
INSERT INTO public.lob_inventory1_stage (lob, ito_unit, itam_ciid, app_instance, tso, tso_status, canonic_alias, name, ip_address, infra, function, type, size, vcpu, memory_gb, fqdn, vc_cluster, vcf_domain, vc_vm_creation_ts, vc_vm_disks_total_gb, vc_vm_size, vc_vm_vcpu, vc_vm_memory_gb, env, guest_ip_address, guest_power_state, guest_id, guest_tools_status, import_timestamp, state)
VALUES 
('IT-Infrastructure', 'ITO-Central', 'CIID-91301', 'IT-APP-1', 'Alice Johnson', 'Active', 'it-stage-001', 'it-stage-001', '192.168.50.101', 'vSphere', 'Load Balancer', 'VM', 'Medium', 4, 16, 'it-stage-001.stage.company.com', 'Cluster-Stage-01', 'Domain-Staging', '2024-04-01 07:00:00', 250, 'Medium', 4, 16, 'staging', '192.168.50.101', 'poweredOn', 'rhel8', 'guestToolsRunning', NOW(), 'active'),

('IT-Infrastructure', 'ITO-Central', 'CIID-91302', 'IT-APP-2', 'Alice Johnson', 'Active', 'it-stage-002', 'it-stage-002', '192.168.50.102', 'vSphere', 'Web Server', 'VM', 'Large', 8, 32, 'it-stage-002.stage.company.com', 'Cluster-Stage-01', 'Domain-Staging', '2024-04-01 07:30:00', 500, 'Large', 8, 32, 'staging', '192.168.50.102', 'poweredOn', 'rhel8', 'guestToolsRunning', NOW(), 'active'),

('IT-Infrastructure', 'ITO-Central', 'CIID-91303', 'IT-APP-3', 'Mike Davis', 'Active', 'it-stage-003', 'it-stage-003', '192.168.50.103', 'vSphere', 'Database', 'VM', 'Large', 8, 32, 'it-stage-003.stage.company.com', 'Cluster-Stage-01', 'Domain-Staging', '2024-04-15 09:00:00', 500, 'Large', 8, 32, 'staging', '192.168.50.103', 'poweredOff', 'rhel8', 'guestToolsNotRunning', NOW(), 'active');


-- ========================================
-- VERIFICATION QUERIES
-- ========================================

-- Count servers by LOB in production
SELECT lob, COUNT(*) as server_count 
FROM public.lob_inventory1 
GROUP BY lob 
ORDER BY lob;

-- Count servers by LOB in staging
SELECT lob, COUNT(*) as server_count 
FROM public.lob_inventory1_stage 
GROUP BY lob 
ORDER BY lob;

-- Check power states
SELECT 
    'Production' as environment,
    guest_power_state, 
    COUNT(*) as count 
FROM public.lob_inventory1 
GROUP BY guest_power_state
UNION ALL
SELECT 
    'Staging' as environment,
    guest_power_state, 
    COUNT(*) as count 
FROM public.lob_inventory1_stage 
GROUP BY guest_power_state;

-- Total resources summary
SELECT 
    'Production' as environment,
    COUNT(*) as total_servers,
    SUM(vc_vm_vcpu) as total_vcpu,
    SUM(vc_vm_memory_gb) as total_memory_gb,
    SUM(vc_vm_disks_total_gb) as total_disk_gb
FROM public.lob_inventory1
UNION ALL
SELECT 
    'Staging' as environment,
    COUNT(*) as total_servers,
    SUM(vc_vm_vcpu) as total_vcpu,
    SUM(vc_vm_memory_gb) as total_memory_gb,
    SUM(vc_vm_disks_total_gb) as total_disk_gb
FROM public.lob_inventory1_stage;