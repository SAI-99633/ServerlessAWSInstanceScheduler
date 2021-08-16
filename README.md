we have created the lambda function to create the ec2 instances and stop, start the instances by using python3.8 version

we have created api endpoint to trigger the lambda funtion by using api gateway in AWS.

The endpoint url is below.

https://jywshguxg3.execute-api.us-east-2.amazonaws.com/create/ec2resource

Please test the api endpoint url in postman by providing the key values as below.

##################  For creating the instance ##############
{
"action":"create"
}

##################  For stopping the instance ##############
{
"action":"stop"
}

##################  For starting the instace ###############
{
"action":"start
}

and please refer the lambda function code which is placed in same repo and named as ec2-create-start-stop.py.
