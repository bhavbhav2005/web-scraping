1)docker cli commands part 1
docker --version
docker pull hello-world
docker run hello-world 
docker ps -a 
docker rm [container-id] 
docker rmi hello-world 
docker pull redis 
docker run --name my-redis -d redis
docker ps 
docker exec -it my-redis redis-cli
SET name "Alice"
 GET name
docker stop my-redis 
docker start my-redis
docker stop my-redis 
docker rm my-redis
docker rmi redis
2)docker cli commands part 2
e C:\DockerProjects\Redis
FROM redis:latest
CMD ["redis-server"] 
docker build -t redisnew .
docker run --name myredisnew -d redisnew
docker ps
docker stop myredisnew
 docker login
docker ps -a
 docker commit 0e993d2009a1 budarajumadhurika/redis1
 docker images
 docker push budarajumadhurika/redis1
 docker rm 0e993d2009a1
 docker rmi budarajumadhurika/redis1
docker ps -a
 docker logout
 docker pull budarajumadhurika/redis1
 docker run --name myredis -d budarajumadhurika/redis1
 docker exec -it myredis redis-cli
SET name "Abcdef"
GET name
exit
docker ps -a
docker rm 50a6e4a9c326
 docker images
docker rmi budarajumadhurika/redis1
docker logout
3)modify and push image
docker pull ubuntu 
docker run -it --name newubuntu -d ubuntu
docker ps 
docker exec -it 885a01bcdbe0 bash
git --version 
apt update 
apt install git -y
git --version
exit
docker stop 885a01bcdbe0
docker commit 885a01bcdbe0 budarajumadhurika/newubuntu2024
docker images
docker login
docker push budarajumadhurika/newubuntu2024
docker logout
docker rm 885a01bcdbe0 
docker rmi budarajumadhurika/newubuntu2024
docker pull budarajumadhurika/newubuntu2024 
docker run --name newubuntu2024 -it budarajumadhurika/newubuntu2024
git --version 
exit 
docker ps -a 
docker rm 28aee36085cb
docker rmi budarajumadhurika/newubuntu2024
4)create and push docker file image
// calculator.js
function add(a, b) {
 return a + b;
}
function subtract(a, b) {
 return a - b;
}
function multiply(a, b) {
 return a * b;
} 
function divide(a, b) {
 if (b === 0) {
 return "Cannot divide by zero!";
 }
 return a / b;
}
// Print the calculated values
console.log("Addition (2 + 3):", add(2, 3));
console.log("Subtraction (5 - 2):", subtract(5, 2));
console.log("Multiplication (4 * 3):", multiply(4, 3));
console.log("Division (10 / 2):", divide(10, 2));
FROM node:16-alpine
WORKDIR /app
COPY calculator.js /app
CMD ["node", "calculator.js"] 
docker build -t simple-calculator . 
docker run simple-calculator
docker login
docker tag simple-calculator your-dockerhub-username/simplecalculator
docker push your-dockerhub-username/simple-calculator 
docker ps -a 
docker rm <container-id>
docker rmi your-dockerhub-username/simple-calculator
docker pull your-dockerhub-username/simple-calculator 
docker run your-dockerhub-username/simple-calculator
docker ps -a
docker rm <container-id> 
docker images
docker rmi <image-id>
docker logout
4)multiple
https://gist.github.com/bradtraversy/faa8de544c62eef3f31de406982f1d42
my_docker_projec:folder
version: '3.1'
services:
 db:
   image: mysql:5.7
 container_name: mysql_container
 environment:
 MYSQL_ROOT_PASSWORD: rootpassword
 MYSQL_DATABASE: wordpress_db
 MYSQL_USER: wordpress_user
 MYSQL_PASSWORD: wordpress_pass
 volumes:
 - db_data:/var/lib/mysql
 wordpress:
 depends_on:
 - db
 image: wordpress:latest
 container_name: wordpress_container
 ports:
 - "8000:80"
 environment:
 WORDPRESS_DB_HOST: db:3306
 WORDPRESS_DB_USER: wordpress_user
 WORDPRESS_DB_PASSWORD: wordpress_pass
 WORDPRESS_DB_NAME: wordpress_db
 volumes:
 - ./wordpress_data:/var/www/html
volumes:
 db_data:
docker-compose up -d 
o http://localhost:8000. 
docker-compose stop
docker-compose start
docker-compose down 
5)minikube
minikube start
kubectl create deployment mynginx --image=nginx 
kubectl get deployments 
kubectl expose deployment mynginx --type=NodePort --port=80 --
target-port=80
kubectl scale deployment mynginx --replicas=4 
kubectl port-forward svc/mynginx 8081:80 
 Open your browser and go to:
http://localhost:8081 
minikube tunnel
minikube service mynginx --url
kubectl delete deployment mynginx
kubectl delete service mynginx
minikube stop
minikube delete 
6)nagios
docker pull jasonrivers/nagios:latest
docker run --name nagiosdemo -p 8888:80 jasonrivers/nagios:latest
localhost:8888
Username: nagiosadmin
Password: nagios
docker ps
docker stop nagiosdemo 
docker rm nagiosdemo
docker images
docker rmi jasonrivers/nagios:latest
7)aws
Step 1: Log in to AWS and Go to EC2
Step 2: Launch an EC2 Instance
Step 3: Connect to the EC2 Instance
1. Select your instance, click Connect, and copy the SSH command.
2. Open PowerShell (Windows) or Terminal (Mac/Linux) on your computer.
3. Navigate to the folder where your .pem file is saved using the cd command.
4. Paste the SSH command and press Enter. Type "yes" if prompted. 
sudo apt update 
sudo apt-get install docker.io
sudo apt install git
sudo apt install nano
<html>
<head><title>My Webpage</title></head>
<body><h1>Hello from AWS!</h1></body>
</html> 
git init
git add .
git commit -m "First commit" 
git remote add origin <Your_Repo_URL>
git push -u origin main
Step 6: Deploy the Web Application Using Docker 
git clone <Your_Repo_URL> 
nano Dockerfile 
FROM nginx:alpine
COPY . /usr/share/nginx/html 
sudo docker build -t my-web-app .
sudo docker run -d -p 80:80 my-web-app
Step 7: Access Your Web Application
In this step, we will view the deployed web page online.
1. Copy the Public IP Address of your EC2 instance from the AWS console.
2. Paste it into your browser (e.g., http://<Public_IP>).
3. You’ll see your web page with the message "Hello from AWS!" displayed
sudo docker ps
sudo docker stop <Container_ID>
8)maven web aws
Step 1: Launch an EC2 Instance
In this step, we will set up a virtual server to host our Maven web project.
1. Log in to AWS: Access your AWS account and navigate to Services > Compute >
EC2.
2. Launch the instance:
o Name: Enter a descriptive name, e.g., MavenWebProjectServer.
o AMI: Select Ubuntu Server (Free Tier Eligible).
o Instance Type: Choose t2.micro.
o Key Pair: Create a key pair or use an existing one. Save the .pem file securely.
o Network Settings: Enable Allow HTTP/HTTPS traffic.
o Storage: Use the default size (8 GB).
3. Click Launch Instance and wait for the status to change to "Running."
4. Note down the Public IP Address from the EC2 dashboard. 
Step 2: Connect to the EC2 Instance
In this step, we will connect to the server.
1. Open PowerShell (Windows) or Terminal (Mac/Linux) and navigate to the folder with
the .pem file using the cd command.
2. Use SSH to connect to the instance:
ssh -i "<KeyFile>.pem" ubuntu@<Public_IP>
Replace <KeyFile> with the .pem file name and <Public_IP> with your
instance’s public IP.
3. If prompted, type "yes" to confirm the connection. 
sudo apt update
sudo apt-get install docker.io -y
sudo apt install git -y
sudo apt install nano -y
git clone <Your_Repo_URL>
cd <Your_Project_Folder>
nano Dockerfile 
FROM tomcat:9-jdk11
COPY target/*.war /usr/local/tomcat/webapps/
sudo docker build -t maven-web-project . 
sudo docker run -d -p 9090:8080 maven-web-project
Step 7: Configure Security Group for Port 9090
We will ensure the EC2 instance allows traffic on port 9090.
1. In the AWS EC2 dashboard, go to Security and click the Security Group ID.
2. Add an inbound rule:
o Type: Custom TCP
o Port Range: 9090
o Source: Anywhere (0.0.0.0/0) or your IP.
3. Save the changes 
http://<Public_IP>:9090/<Your_Project_Name> 
sudo docker ps
sudo docker stop <Container_ID> 
8)script
pipeline {
 agent any
 tools {
 maven 'MAVEN_HOME'
 }
 stages {
 stage('git repo & clean') {
 steps {
 bat "rmdir /s /q SampleMavenJavaProject"
 bat "git clone
https://github.com/budarajumadhurika/SampleMavenJavaProject.gi
t"
 bat "mvn clean -f SampleMavenJavaProject"
 }
 }
 stage('install') {
 steps {
 bat "mvn install -f SampleMavenJavaProject"
 }
 }
 stage('test') {
 steps {
 bat "mvn test -f SampleMavenJavaProject"
 }
 }
 stage('package') {
 steps {
 bat "mvn package -f SampleMavenJavaProject"
 }
 }
 }
} 
