# import streamlit as st
# import pandas as pd

# # Load datasets
# df_fake = pd.read_pickle(r"C:\Users\kalyan nagu\OneDrive\Desktop\hello\df_fake.pkl")
# df_true = pd.read_pickle(r"C:\Users\kalyan nagu\OneDrive\Desktop\hello\df_true.pkl")

# # Streamlit UI
# st.title("Fake News Detection Dataset")

# # Show dataset selection
# dataset_option = st.selectbox("Select Dataset", ["Fake News", "True News"])

# if dataset_option == "Fake News":
#     st.write(df_fake.head())  # Show first few rows
# else:
#     st.write(df_true.head())

# # Search functionality
# search_query = st.text_input("Search for a headline:")
# if search_query:
#     filtered_df = df_fake[df_fake['title'].str.contains(search_query, case=False, na=False)] if dataset_option == "Fake News" else df_true[df_true['title'].str.contains(search_query, case=False, na=False)]
#     st.write(filtered_df)

# # Run with: `streamlit run your_script.py`


import streamlit as st
import pickle

# Load the trained model
model_path = r"C:\Users\kalyan nagu\OneDrive\Desktop\hello\fake_news_model.pkl"
with open(model_path, "rb") as f:
    model = pickle.load(f)

# Streamlit UI
st.title("📰 Fake News Detector")

# User input
user_input = st.text_area("Enter a news headline or article:")

if st.button("Check"):
    if user_input.strip():
        # Predict
        prediction = model.predict([user_input])[0]
        result = "✅ True News" if prediction == 1 else "🚨 Fake News"
        st.subheader(result)
    else:
        st.warning("Please enter some text.")

# Run with: `streamlit run app.py`
