# Q1 Here <value> is the probability of getting a credit card. You need to choose the right one.
## options:
* 0.3269
* 0.5269
* 0.7269 <-
* 0.9269
## Answer: {'get_credit': True, 'get_credit_probability': 0.726936946355423}

# Q2 What's the version of kind that you have?

## Version:
`kind --version`

`kind version 0.20.0`

# Q3 Now let's test if everything works. Use kubectl to get the list of running services. What's CLUSTER-IP of the service that is already running there?
## answer:
* kubectl get services
* NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
* kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   55s

# Q4 What's the command we need to run for that?
## Answer: kind load docker-image

# Q5 What is the value for <Port>?
## Answer: 9696

# Q6 Fill it in. What do we need to write instead of <???>?
## credit-card

# Q7 What was the maximum amount of the replicas during this test?
## Answer: 3