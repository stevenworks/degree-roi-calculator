# Degree ROI Calculator

## Overview
The **Degree ROI Calculator** helps students and professionals evaluate the return on investment (ROI) of their degree program by comparing the total cost of the degree (tuition + living expenses) against their potential lifetime salary. It gives you insight into how long it will take to pay off your degree and the overall financial benefit over a 40-year career.

This project is built using **Streamlit**, a Python framework for building interactive web apps.

## Features
- Calculate the total cost of a degree (tuition and living expenses).
- Estimate the time it will take to pay off the degree based on expected salary.
- Visualize the net value of your degree over 40 years.
- Generate a unique shareable link to share your results with others.

## How it Works
1. **Input your degree details**:
   - Select your major.
   - Enter your expected starting salary or use the average salary for your selected major.
   - Set your tuition and living cost per year.
   - Choose the number of years it will take you to complete your degree.

2. **View your results**:
   - See how long it will take to pay off your degree.
   - Get a lifetime ROI estimate.
   - Visualize your net value over time in a graph.

3. **Share your results**:
   - Once you’ve entered your details, a unique link will be generated that you can share with others. This link will show them the same results based on your inputs, making it easy to compare with friends and peers.

## How to Run the Project Locally

1. Clone this repository:
   ```bash
   git clone https://github.com/stevenworks/degree-roi-calculator.git
   cd degree-roi-calculator
   ```
Install dependencies:
```bash
pip install -r requirements.txt
```
Run the Streamlit app:

```bash
streamlit run app.py
```
Visit http://localhost:8501 in your web browser to interact with the app.

## Customization
You can customize the following in the app:

Salary Data: Modify the average salary data for each major in the average_salaries dictionary.

Design: Customize the look and feel by editing the Streamlit elements in app.py.

## Future Enhancements
User Authentication: Allow users to create accounts to save their results and track their progress over time.

Additional Financial Data: Integrate real-world data about average salaries, tuition, and career advancement.

Expanded ROI Calculation: Include additional factors such as job growth rates, inflation, and career shifts.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

Enjoy calculating and sharing your degree's ROI! 📚💰
