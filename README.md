## Student responses to the PISA 2012 statement "Math is One of My Best Subjects"

<p>View the visualization here: https://bl.ocks.org/aarongruberg/raw/1a703bfe4d4ad8b6e05b400557ffd119/ </p>

<p>Link to PISA 2012 Dataset and PISA Data Dictionary: https://docs.google.com/document/d/1w7KhqotVi5eoKE3I_AZHbsxdr-NmcWsLTIiZrpxWx4w/pub?embedded=true </p>

<p>The PISA survey was given to 480,174 students from 65 Countries and asked students about their experience with and feelings toward reading, math, and science.  I split the students into groups with low, moderate, or high study time and created a layered bar chart of their responses to the statement "Math is One of My Best Subjects."  Around half of the students with high study time felt very confident in math but more study time did not always mean higher confidence in math.  Around a quarter of students with low study time and a quarter of students with high study time both felt very weak in math.</p>

<p>I wrote one python script 'clean_pisa.py' to clean the data and select columns I was interested in, and another script 'my_pisa.py' to split the students into groups for students with low, moderate, or high out of school study time.  I created a D3 barchart 'index.html' with layered bars for each study group as well as individual charts for each group that can be viewed by clicking on the "low", "moderate", "high", and "all" buttons in the visualization.</p>