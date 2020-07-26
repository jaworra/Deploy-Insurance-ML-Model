# Online Model Deploy
Build and deploy your machine learning web app

# Requirements
PyCaret, Flask, Docker, Streamlit


# Tips for stream lit
Prior to deploying model. Run locally with the following commands
Anaconda prompt in folder: streamlit run app.py


# process steps
1. ECR in aws - create repo and push
2. Config cluster - network only , Task definition -fargate memory:0.5gb cpu: 0.25 , add container
3. Run task, select vps and configure with inbound 8501, update security group via GUID edit security group with inbount TCP 8501.
4. Check public IP with port for served model. 