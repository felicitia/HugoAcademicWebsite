---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Empirically Assessing Opportunities for Prefetching and Caching in Mobile Apps (ASE 2018)"
event: Automated Software Engineering (ASE)
event_url:
location: Montpellier, France
summary:
abstract: "Network latency in mobile software has a large impact on user experience, with potentially severe economic consequences. Prefetching and caching have been shown effective in reducing the latencies in browser-based systems. However, those techniques cannot be directly applied to the emerging domain of mobile apps because of the differences in network interactions. Moreover, there is a lack of research on prefetching and caching techniques that may be suitable for the mobile app domain, and it is not clear whether such techniques can be effective or whether they are even feasible. This paper takes the first step toward answering these questions by conducting a comprehensive study to understand the characteristics of HTTP requests in over 1,000 popular Android apps. Our work focuses on the prefetchability of requests using static program analysis techniques and cacheability of resulting responses. We find that there is a substantial opportunity to leverage prefetching and caching in mobile apps, but that suitable techniques must take into account the nature of apps’ network interactions and idiosyncrasies such as untrustworthy HTTP header information. Our observations provide guidelines for developers to utilize prefetching and caching schemes in app development, and motivate future research in this area"

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2018-09-06T14:00:00
date_end: 
all_day: false

# Schedule page publish date (NOT talk date).
# publishDate: 2019-09-26T18:09:26-07:00

authors: ["Yixue Zhao", "Paul Wat", "Marcelo Schmitt Laser", "Nenad Medvidović"]
tags: []

# Is this a featured talk? (true/false)
featured: true

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
url_slides: https://speakerdeck.com/yixue_zhao/empirically-assessing-opportunities-for-prefetching-and-caching-in-mobile-apps

url_code:
url_pdf: https://dl.acm.org/citation.cfm?doid=3238147.3238215
url_video: https://youtu.be/iT1pNy370ZM

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
