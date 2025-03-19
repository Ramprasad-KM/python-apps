This is an example Python app which runs in Kubernetes as a service and makes use of multiprocessing. It exposes these APIs:
    /start - kills all processes and starts 5 processes which keep running
    /stop - stops running processes
    /status - gets the number of running processes

**Note**: Follow all the steps if you want to build the app locally and deploy. Otherwise, skip steps 1-4 and start from step-5

1. pip install flask

2. docker build -t my-flask-app .

3. docker tag my-flask-app your-docker-repo/my-flask-app:v1

4. docker push your-docker-repo/my-flask-app:v1

5. kubectl apply -f deployment.yaml

6. kubectl apply -f service.yaml

7. kubectl get svc flask-service

Start processes - curl -X POST http://EXTERNAL-IP/start

Stop processes - curl -X POST http://EXTERNAL-IP/stop

Get status - curl -X GET http://EXTERNAL-IP/status
