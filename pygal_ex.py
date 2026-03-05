import pygal

pie = pygal.Pie()

pie.title = "Time spend on social media"
pie.add("Facebook", var)
pie.add("Instagram", 30)
pie.add("Twitter", 10)
pie.add("LinkedIn", 5)

pie.render_in_browser()