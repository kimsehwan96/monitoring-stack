from yaml import load, FullLoader
from jinja2 import Environment, FileSystemLoader

values = load(open('values.yaml'), Loader=FullLoader)

env = Environment(loader=FileSystemLoader('./'))

template = env.get_template('alertmanager/config/alertmanager.yaml.j2')
render = template.render(values)
with open('./alertmanager/config/alertmanager.yaml', 'w') as f:
    f.write(render)

template = env.get_template('grafana/grafana.ini.j2')
render = template.render(values)
with open('./grafana/grafana.ini', 'w') as f:
    f.write(render)

template = env.get_template('grafana-provisioning/alerting/alerting.yaml.j2')
render = template.render(values)
with open('./grafana-provisioning/alerting/alerting.yaml', 'w') as f:
    f.write(render)

template = env.get_template('docker-compose.yaml.j2')
render = template.render(values)
with open('./docker-compose.yaml', 'w') as f:
    f.write(render)

template = env.get_template('prometheus/config/prometheus.yaml.j2')
render = template.render(values)
with open('./prometheus/config/prometheus.yaml', 'w') as f:
    f.write(render)
