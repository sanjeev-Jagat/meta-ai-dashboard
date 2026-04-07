st.subheader("ROAS Prediction 📊")

headline = st.text_input("Enter Headline")
text = st.text_area("Enter Ad Text")

if st.button("Predict ROAS"):

    if headline == "" or text == "":
        st.error("⚠️ Please enter headline & text")
    else:
        # Feature creation
        hl_len = len(headline)
        txt_len = len(text)

        score = 0

        # Logic based scoring
        if "7" in headline:
            score += 1
        if "free" in text.lower():
            score += 1
        if "doctor" in text.lower():
            score += 1
        if hl_len < 25:
            score += 1

        # ROAS calculation
        roas = round(1.5 + score * 0.7, 2)

        st.success(f"💰 Expected ROAS: {roas}")
