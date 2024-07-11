# monitoring-stack

grafana + prometheus 기반의 모니터링 스택을 템플릿화 한 레포입니다. jinja2 로 템플리팅하였으며 

몇 가지 값만 수정하여서 바로 서버에 적용 할 수 있습니다.

TODO: Add diagram for this stack

## Prerequisite

- Docker >= ?
- Docker-compose >= 1.27.4
- Python3.x (Recommend python3.7 above)


## Components

- Grafana:v10.2.2
- Prometheus:v2.45.1
- Alertmanager:v0.25.0

- Cadvisor:latest (TODO: Fix specific version)

- Node exporter:v1.6.1
- Systemd exporter:v0.6.0
- Process exporter:0.7.10

## How to install

`$ vim values.yaml`

- 필요로 하는 값 수정

`$ ./run.sh`

## Cutomization

`values.yaml` 의 값을 수정해서 사용한다.

## grafana 접근

### Recommend

Route53 을 이용해 `{server_name}-grafana.example.com`(예시) 을 해당 서버의 IP를 바라보도록 A레코드를 생성하고

`Nginx`를 사용하여 리버스 프록시를 해 접근하는것을 추천합니다.

`/etc/nginx/conf.d/grafana.conf`

```conf
server {
    listen       80;
    server_name  myserver-grafana.example.com;

    location / {
	    proxy_pass http://127.0.0.1:3000;
	    proxy_set_header Host $host;
	    proxy_set_header X-Real-IP $remote_addr;
	    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
	    proxy_set_header X-Forwarded-Host $host;
    }
}
```

그 외 기타 이 그라파나 서비스에 접근 할 수 있는 방법을 세팅하면 뭐든 괜찮습니다.


## Reverse Proxy 가 없는 경우

`grafana/grafana.ini.j2` 파일 내에

`root_url` 을 `%(protocol)s://%(domain)s:%(http_port)s/` 로 수정해서 사용한다. 
