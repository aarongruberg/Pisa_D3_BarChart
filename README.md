## Student responses to the PISA 2012 statement "Math is One of My Best Subjects"

<p>View the visualization here: https://bl.ocks.org/aarongruberg/raw/1a703bfe4d4ad8b6e05b400557ffd119/ </p>

<p>Link to PISA 2012 Dataset and PISA Data Dictionary: https://docs.google.com/document/d/1w7KhqotVi5eoKE3I_AZHbsxdr-NmcWsLTIiZrpxWx4w/pub?embedded=true </p>

<p>SUMMARY:</p> 

<p>
The PISA survey was given to 480,174 students from 65 Countries and asked students about their experience with and feelings toward reading, math, and science. I split the students into groups with low, moderate, or high study time and created a layered bar chart of their responses to the statement 'Math is One of My Best Subjects.' 43% of students with high study time strongly agreed that math was among their best subjects, but more study time did not always lead to higher confidence. 27% of students with low study time and 24% of students with high study time strongly disagreed with the statement.</p>

<p>DESIGN:</p>

<p>
 I wrote a script 'clean_pisa.py' to clean the data and select columns I was interested in, and another 'my_pisa.py' to split the students into groups for students with low, moderate, or high out of school study time.  I created a D3 barchart 'index.html' with layered bars for each study group as well as individual charts for each group that can be viewed by clicking on the hour range buttons in the visualization.  After getting feedback, I changed the button labels and color scheme, and added more clear directions for interaction.</p>

<p>FEEDBACK:</p> 

<p>
Person1: Even though people should realize that they have to click on the charts to select them, you might want to consider writing something to make what they need to do more obvious. Click below to select chart or select chart by clicking below, or anything that urges readers to interact with the chart.  Person2: The legend should be the number of hours studied instead of low/med/high.  Also, gradations of a single hue may be more understandable for the stacked graphs.  Person3: The low, moderate, or high study time is not very well explained from just looking at the chart.  I also don't understand how the hover works.  It seems like it tells you the number of an arbitrary block color.  Also, the order of the axis isn't intuitive.  Should go from strongly agree, down to agree, down to disagree, down to strongly disagree.
</p>

<p>RESOURCES:</p>

<p>https://discussions.udacity.com/t/eda-for-1gb-data-set/163124/2</p>
<p>http://bl.ocks.org/gaborsar/raw/56d225b31c1eaf24eccb/</p>
<p>http://bl.ocks.org/gaborsar/raw/2fee16eed782f7ed1e2c/</p>
<p>https://www.oecd.org/pisa/pisaproducts/PISA12_stu_codebook.pdf</p>
<p>https://bl.ocks.org/hrecht/f84012ee860cb4da66331f18d588eee3</p>
<p>http://bl.ocks.org/kiranml1/6872226</p>
<p>https://bl.ocks.org/mbostock/3019563</p>
<p>https://www.oecd.org/pisa/pisaproducts/PISA%202012%20Technical%20Report_Chapter%2016.pdf</p>
<p>https://www.youtube.com/watch?v=8jvoTV54nXw</p>