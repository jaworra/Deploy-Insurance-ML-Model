from pycaret.regression import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np

model = load_model('deployment_26072020')

def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    return predictions

def run():

    from PIL import Image
    image = Image.open('logo2.png')
    image_hospital = Image.open('hospital.jpg')

    st.image(image,use_column_width=False)

    add_selectbox = st.sidebar.selectbox(
    "How would you like to predict?",
    ("Online", "Batch"))

    st.sidebar.info('This app is created to predict patient hospital charges')
    st.sidebar.success('https://www.pycaret.org')
    
    st.sidebar.image(image_hospital)

    st.title("Insurance Charges Prediction App")

    if add_selectbox == 'Online':

        age = st.number_input('Age', min_value=1, max_value=100, value=25)
        sex = st.selectbox('Sex', ['male', 'female'])
        bmi = st.number_input('BMI', min_value=10, max_value=50, value=10)
        children = st.selectbox('Children', [0,1,2,3,4,5,6,7,8,9,10])
        if st.checkbox('Smoker'):
            smoker = 'yes'
        else:
            smoker = 'no'
        region = st.selectbox('Region', ['southwest', 'northwest', 'northeast', 'southeast'])

        output=""

        input_dict = {'age' : age, 'sex' : sex, 'bmi' : bmi, 'children' : children, 'smoker' : smoker, 'region' : region}
        input_df = pd.DataFrame([input_dict])

        if st.button("Predict"):
            output = predict(model=model, input_df=input_df)
            output = '$' + str(output)

        st.success('The output is {}'.format(output))

    if add_selectbox == 'Batch':

        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])

        if file_upload is not None:
            data = pd.read_csv(file_upload)
            predictions = predict_model(estimator=model,data=data)
            st.write(predictions)

if __name__ == '__main__':
    run()

















































# import pandas as pd
# import numpy as np

# from pycaret.regression import *

# #insurance data frame
# data_df=pd.read_csv('data/insurance.csv')
# data_df.info()

# r2 = setup(data_df, target = 'charges', session_id = 123,
#            normalize = True,
#            polynomial_features = True, trigonometry_features = True,
#            feature_interaction=True, 
#            bin_numeric_features= ['age', 'bmi'])

# print(r2)


# # Model Training and Validation 
# lr = create_model('lr')

# # plot residuals of trained model
# plot_model(lr, plot = 'residuals')




# # Import dataset from pycaret repository
# from pycaret.datasets import get_data
# insurance = get_data('insurance')

# # Initialize environment
# from pycaret.regression import *
# r1 = setup(insurance, target = 'charges', session_id = 123,
#            normalize = True,
#            polynomial_features = True, trigonometry_features = True,
#            feature_interaction=True, 
#            bin_numeric_features= ['age', 'bmi'])

# # Train a linear regression model
# lr = create_model('lr')

# # save transformation pipeline and model  
# save_model(lr, model_name = 'model/pycaret-deployment-aws/deployment_26072020')