config = {
     'bootstrap.servers': '<bootstrap-server-endpoint>',     
     'security.protocol': 'SASL_SSL',
     'sasl.mechanisms': 'PLAIN',
     'sasl.username': '<CLUSTER_API_KEY>', 
     'sasl.password': '<CLUSTER_API_SECRET>'}
sr_config = {
    'url': '<schema.registry.url>',
    'basic.auth.user.info':'<SR_API_KEY>:<SR_API_SECRET>'
}