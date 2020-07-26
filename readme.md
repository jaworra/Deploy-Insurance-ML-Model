# Deploy-Insurance-ML-Model
Build and deploy your machine learning web app

# Requirements
PyCaret, Docker, Streamlit, AWS


# Tips for stream lit
Prior to deploying model. Run locally with the following commands
Anaconda prompt in folder: streamlit run app.py
<<<<<<< HEAD


# process steps
1. ECR in aws - create repo and push
2. Config cluster - network only , Task definition -fargate memory:0.5gb cpu: 0.25 , add container
3. Run task, select vps and configure with inbound 8501, update security group via GUID edit security group with inbount TCP 8501.
4. Check public IP with port for served model. 
=======
>>>>>>> a2204476918add0afaaf07efb2a9878e2fa7f61e
