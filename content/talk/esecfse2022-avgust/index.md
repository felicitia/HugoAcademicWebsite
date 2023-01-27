---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Avgust: Automating Usage-Based Test Generation from Videos of App Executions [ESEC/FSE 2022 Presentation]"
event: The ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering (ESEC/FSE)
event_url:
location: Singapore
address:
  street:
  city:
  region:
  postcode:
  country:
summary:
abstract: "Writing and maintaining UI tests for mobile apps is a time-consuming and tedious task. While decades of research have produced automated approaches for UI test generation, these approaches typically focus on testing for crashes or maximizing code coverage. By contrast, recent research has shown that developers prefer usage-based tests, which center around specific uses of app features, to help support activities such as regression testing. Very few existing techniques support the generation of such tests, as doing so requires automating the difficult task of understanding the semantics of UI screens and user inputs. In this paper, we introduce Avgust, which automates key steps of generating usage-based tests. Avgust uses neural models for image understanding to process video recordings of app uses to synthesize an app-agnostic state-machine encoding of those uses. Then, Avgust uses this encoding to synthesize test cases for a new target app. We evaluate Avgust on 374 videos of common uses of 18 popular apps and show that 69% of the tests Avgust generates successfully execute the desired usage, and that Avgust's classifiers outperform the state of the art."

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: 2022-11-15T18:00:00
date_end: 
all_day: false

# Schedule page publish date (NOT talk date).
# publishDate: 2020-11-11T18:09:40-07:00

authors: ["Yixue Zhao", "Saghar Talebipour", "Kesina Baral", "Hyojae Park", "Leon Yee", "Safwat Ali Khan", "Yuriy Brun", "Nenad Medvidovic", "Kevin Moran"]
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
url_slides: https://speakerdeck.com/yixue_zhao/avgust-automating-usage-based-test-generation-from-videos-of-app-executions

url_code:
url_pdf: https://arxiv.org/abs/2209.02577
url_video: https://youtu.be/LB-TrLhQcvI

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