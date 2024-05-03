---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Assessing the Feasibility of Web-Request Prediction Models on Mobile Platforms [MOBILESoft 2021 Paper Presentation]"
event: International Conference on Mobile Software Engineering and Systems (MOBILESoft 2021)
event_url:
location: Virtual Event
address:
  street:
  city:
  region:
  postcode:
  country:
summary:
abstract: "Prefetching web pages is a well-studied solution to reduce network latency by predicting users' future actions based on their past behaviors. However, such techniques are largely unexplored on mobile platforms. Today's privacy regulations make it infeasible to explore prefetching with the usual strategy of amassing large amounts of data over long periods and constructing conventional, \"large\" prediction models. Our work is based on the observation that this may not be necessary: Given previously reported mobile-device usage trends (e.g., repetitive behaviors in brief bursts), we hypothesized that prefetching should work effectively with \"small\" models trained on mobile-user requests collected during much shorter time periods. To test this hypothesis, we constructed a framework for automatically assessing prediction models, and used it to conduct an extensive empirical study based on over 15 million HTTP requests collected from nearly 11,500 mobile users during a 24-hour period, resulting in over 7 million models. Our results demonstrate the feasibility of prefetching with small models on mobile platforms, directly motivating future work in this area. We further introduce several strategies for improving prediction models while reducing the model size. Finally, our framework provides the foundation for future explorations of effective prediction models across a range of usage scenarios."

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2021-05-17
date_end: 
all_day: true

# Schedule page publish date (NOT talk date).
# publishDate: 2019-09-26T18:08:57-07:00

authors: ["Yixue Zhao", 
"Siwei Yin", 
"Adriana Sejfia", 
"Marcelo Schmitt Laser", 
"Haoyu Wang", 
"Nenad Medvidovic"]
tags: []

# Is this a featured talk? (true/false)
featured: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
links:
- name: Subscribe
  url: https://www.youtube.com/channel/UCn-EdIQUp1jZI1zahbXYLBw
  icon_pack: fab
  icon: youtube

# Optional filename of your slides within your talk's folder or a URL.
url_slides: https://speakerdeck.com/yixue_zhao/assessing-the-feasibility-of-web-request-prediction-models-on-mobile-platforms

url_code:
url_pdf: https://arxiv.org/abs/2011.04654
url_video: https://youtu.be/91b3juLFbeU

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---
