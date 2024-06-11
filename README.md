# Mithril-Security-Skill-Assessment
This repository is made for Mithril Security Skill assessment, code logic and how to run can be found below.

## How to run the codes using docker:

If you are using Macbook you may skip steps 3 and 4. If running from Kali-Linux please follow all the steps to ensure proper execution of the code.

1. ```sudo systemctl enable docker --now```

2. ```docker```

3. ```sudo apt-get install qemu qemu-user-static```

4. ```sudo docker run --rm --privileged multiarch/qemu-user-static --reset -p yes```

5. ```sudo docker run --platform linux/arm64 plann1ng/task_1a_image```

6. ```sudo docker run --platform linux/arm64 plann1ng/task_1b_image```

7. ```sudo docker run --platform linux/arm64 plann1ng/task_1a_image python ./tests.py```

8. ```sudo docker run --platform linux/arm64 plann1ng/task_1b_image python ./tests.py```

## Task_1a
Rather simple logic for this code, where we have a given list with size *(n)* and we compare *(n)th* index to the *(n-1)th* by start iteration from [1]. If the current index price is bigger than the previous index price it will indicate a buying opportunity so we buy.




## Task_1b
Same logic, however the oly difference now is that we have two lists to iterate over. We start by adding the [0] index of the risk always from low-risk since if we pick high-risk it is not possible to take previous index *(n-1)* as 0 risk, while technically that is not possible if there was such a case where each week number was different and not the same or if we ourselves have een defining if the week is going to be low or high risk by taking how many profitable days we could take from each day of the given could have been more interesting this is so far the solution. All that said after initializing the first index we do simply compare the high-risk and low-risk list and in case for the given week high-risk R:R (Risk-Reward) ratio is higher than low-risk list we do keep track of the last added item to the total value, and then we substract this last added item from the total value which will indicate that previous week was 0 risk. Then we simply update our last added variable to the current found value and in the end adding it to the total value, and in case low-risk is equal or higher than the high-risk we add the low-risk to our total number.

## Benchmarking:
Benchmark of the task 1a is approximately **7.24 us**, while task 1b be sitting at around **2.35 us**, which I believe are quite efficient and rather fast.

## Task 2
### Assumptions (Hypotheses):
1. User devices can manage digital certificates.
2. The Kubernetes cluster is secured with proper network policies.
3. The secure enclave can validate access tokens (JWT).
4. Intermediate CA is trusted and securely managed.
5. User devices support MFA mechanisms.
6. Kubernetes uses a secure service mesh.
7. Intermediate CA and OCSP Responder are highly available.
8. JWTs are securely signed using HSM.
9. IAM efficiently manages user roles and permissions.

### Outline
User Device: This is where users start their authentication process. It is assumed that user devices can store and manage digital certificates and support Multi-Factor Authentication (MFA) mechanisms.

License Server: This server handles user registrations and authentications. During user registration, it generates a Certificate Signing Request (CSR) on behalf of the user and uses MFA to verify the user's identity. For authentication, it verifies the certificate and issues a JWT (JSON Web Token).

Intermediate CA (Certificate Authority): This is part of the PKI infrastructure that handles certificate issuance. The Intermediate CA generates and signs certificates, which are used to authenticate users. It operates within a secure Kubernetes (K8s) environment, ensuring secure management.

Secure Enclave: This is a highly secure environment where sensitive operations are performed. Users access the secure enclave using the JWT issued by the license server. The secure enclave validates these tokens.

OCSP/CRL Responder: This component ensures that certificates are still valid by checking their status in real-time (OCSP) or from a list of revoked certificates (CRL). It is deployed with high availability in Kubernetes.

Kubernetes (K8s) Cluster: The whole architecture is deployed on a Kubernetes cluster, which manages and orchestrates the deployment, scaling, and operations of the components. This includes secure network policies and a service mesh for enhanced security.


# Final words
Tried to avoid too much complication on the code, tests for both codes can be run using docker by using the commands stated above. It was fun assignment especially the second part, even though I was not aware of some of the findings, I would say it looks good considering the short amount of time, since I saw the e-mail has been filtered out in the promotions section. 

### Benchmarker for Python
https://perfpy.com/static/dist/#/3.9






