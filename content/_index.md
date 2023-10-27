---
title: About me
type: docs
---

<table style="border-collapse: collapse; width: 100%; border: none">
  <tr>
    <td style="width: 20%; vertical-align: top; padding-right: 20px; border: none">
    <img src="me.jpeg" style="border-radius: 15%; float: left; padding-right: 15px" width="250">
    </td>
    <td style="width: 50%; vertical-align: top; border: none">
      <p style="font-size: 20px;">
        Ph.D. Candidate<br>
        Department of Electrical and Computer Engineering<br>
        University of Toronto<br>
        Vector Institute for Artificial Intelligence<br>
        <p style="font-size: 14;">
            <a href="https://dsevero.com/cv.pdf"> CV (last updated: October/2023) </a> |
            <a href="https://twitter.com/_dsevero"> Twitter </a> |
            <a href="https://scholar.google.com/citations?user=5bQjLz4AAAAJ"> Google Scholar </a> |
            <a href="https://github.com/dsevero"> GitHub </a>
        </p>
     </p>
    </td>
  </tr>
</table>


# Research
My research interests are generative modelling, information theory, and compression under computational and memory constraints.
Data sources usually have some type of structure, such as graphs and sets.
This means we can model and compress them better by taking this structure into account.
Unfortunately, existing methods that do this are either sub-optimal (don't achieve the Shannon bound) or computationally intractable.
I’m interested in building computationally efficient compression algorithms that can be used with deep generative models on structured data, as well as their connections to bayesian methods.

Originally, I am from Florianópolis (Brazil) but I've lived in New Jersey, Orlando, Toronto (now), São Paulo, as well as other smaller cities in the south of Brazil.

Previously, I've interned at the [Fundamental AI Research (FAIR) lab](https://ai.facebook.com/) at Meta with [Karen Ullrich](https://karenullrich.info/) in the summer of 2021.

I spent 2022 at [Google AI](https://ai.google/) with [Lucas Theis](http://theis.io/) and [Johannes Ballé](https://balle.io/) as a Student Researcher.

---

# Latest News
**August/2023** - I started a second internship at FAIR (Meta AI) in information theory and generative modelling with [Matthew Muckley](https://mmuckley.github.io/)

**April/2023** - [Random Edge Coding](https://arxiv.org/abs/2305.09705) and [Action Matching](https://arxiv.org/abs/2210.06662) were accepted to ICML 2023

**March/2023** - Check out our [ICML 2023 Workshop on Neural Compression and Information Theory](https://neuralcompression.github.io/workshop23)

**February/2023** - I was selected as a finalist for the Meta Research PhD Fellowship, 2023. [Congrats to all the winners](https://research.facebook.com/blog/2023/4/announcing-the-2023-meta-research-phd-fellowship-award-winners/)!

# Selected Publications and Preprints
For a complete list, please see my [Google Scholar](https://scholar.google.com/citations?user=5bQjLz4AAAAJ&hl=en) profile.


<figure>
  <img src="lasi-thumbnail.png" style="float: left; margin-right: 10px; width: 200px;">
  <figcaption>
    <b>The Unreasonable Effectiveness of Linear Prediction as a Perceptual Metric</b><br>
    <u>Daniel Severo</u>, Lucas Theis, Johannes Ballé<br>
    Preprint, 2023 <br>
    <a href="https://arxiv.org/abs/2310.05986"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat"></a>
    <a href="https://github.com/dsevero/Linear-Autoregressive-Similarity-Index"><img src="https://img.shields.io/badge/code-grey.svg?logo=github&style=flat"></a>
    <br>
  </figcaption>
</figure>

---

<figure>
  <img src="rec.svg" style="float: left; margin-right: 10px; width: 200px;">
  <figcaption>
    <br>
    <b>Random Edge Coding: One-Shot Bits-Back Coding of Large Labeled Graphs</b><br>
    <u>Daniel Severo</u>, James Townsend, Ashish Khisti, Alireza Makhzani<br>
    International Conference on Machine Learning (ICML), 2023 <br>
    <a href="https://arxiv.org/abs/2305.09705"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat"></a>
    <a href="https://github.com/dsevero/Random-Edge-Coding"><img src="https://img.shields.io/badge/code-grey.svg?logo=github&style=flat"></a>
    <br>
  </figcaption>
</figure>

---
<figure>
  <img src="am-thumbnail.png" style="float: left; margin-right: 10px; width: 200px;">
  <figcaption>
    <br>
    <b>Action Matching: Learning Stochastic Dynamics from Samples</b><br>
    Kirill Neklyudov, Rob Brekelmans, <u>Daniel Severo</u>, Alireza Makhzani<br>
    International Conference on Machine Learning (ICML), 2023 <br>
    <a href="https://arxiv.org/abs/2210.06662"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat"></a>
    <a href="https://github.com/necludov/jam"><img src="https://img.shields.io/badge/code-grey.svg?logo=github&style=flat"></a>
    <a href="https://www.youtube.com/watch?v=35uEI5ryDRQ"><img src="https://img.shields.io/badge/video-0A75AD.svg?logo=youtube&style=flat"></a>
    <br>
  </figcaption>
</figure>

---
<figure>
  <img src="bbms-thumbnail-pop.png" style="float: left; margin-left: 30px; margin-right: 50px; width: 130px;">
  <figcaption>
    <b>Compressing Multisets with Large Alphabets using Bits-Back Coding</b><br>
    <u>Daniel Severo</u>, James Townsend, Ashish Khisti, Alireza Makhzani, Karen Ullrich<br>
    IEEE Journal on Selected Areas in Information Theory, 2023<br>
    <span style="color:red"><b>Best Paper Award</b></span> at NeurIPS Workshop on DGMs, 2021<br>
    <a href="https://arxiv.org/abs/2107.09202"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat"></a>
    <a href="https://github.com/facebookresearch/multiset-compression"><img src="https://img.shields.io/badge/code-grey.svg?logo=github&style=flat"></a>
    <a href="https://youtube.com/watch?v=Gwf9_t-JjsQ"><img src="https://img.shields.io/badge/video-0A75AD.svg?logo=youtube&style=flat"></a>
    <a href="https://dsevero.com/severo-townsend-dcc22-multisets.pdf"><img src="https://img.shields.io/badge/slides-065535.svg?logo=latex&style=flat"></a>
    <br>
  </figcaption>
</figure>

---
<figure>
  <img src="wyner-thumbnail-2.png" style="float: left; margin-right: 40px; width: 170px;">
  <figcaption>
    <b>Data-driven Optimization for Zero-delay Lossy Source Coding with Side-Information</b><br>
    Elad Domanovitz, <u>Daniel Severo</u>, Ashish Khisti, Wei Yu<br>
    International Conference on Acoustics, Speech, & Signal Processing (ICASSP), 2022<br>
    <a href="https://ieeexplore.ieee.org/document/9747823"><img src="https://img.shields.io/badge/IEEE-blue.svg?style=flat"></a>
    <br>
    <br>
  </figcaption>
</figure>

---
<figure>
  <img src="rcaq-thumbnail-2.png" style="float: left; margin-right: 40px; width: 170px;">
  <figcaption>
    <br>
    <b>RCAQ: Regularized Classification-Aware Quantization</b><br>
    <u>Daniel Severo</u>, Elad Domanovitz, Ashish Khisti<br>
    Biennial Symposium on Communications (BSC), 2021<br>
    <a href="https://arxiv.org/abs/2107.09716"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat"></a>
    <a href="https://github.com/dsevero/rcaq"><img src="https://img.shields.io/badge/code-grey.svg?logo=github&style=flat"></a>
    <br>
  </figcaption>
</figure>

---
<figure>
  <img src="mcbits-thumbnail-2.png" style="float: left; margin-right: 30px; width: 180px;">
  <figcaption>
    <b>Improving Lossless Compression Rates via Monte Carlo Bits-Back Coding</b><br>
    Yangjun Ruan*, Karen Ullrich*, <u>Daniel Severo*</u>, James Townsend, Ashish Khisti, Arnaud Doucet, Alireza Makhzani, Chris J. Maddison<br>
    <span style="color:red"><b>Long talk</b></span> at International Conference on Machine Learning (ICML), 2021<br>
    <a href="https://arxiv.org/abs/2102.11086"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat"></a>
    <a href="https://github.com/ryoungj/mcbits"><img src="https://img.shields.io/badge/code-grey.svg?logo=github&style=flat"></a>
    <a href="https://slideslive.com/38958684/improving-lossless-compression-rates-via-monte-carlo-bitsback-coding?ref=speaker-25566-latest&locale=e"><img src="https://img.shields.io/badge/video-0A75AD.svg?logo=slides&style=flat"></a>
    <br>
  </figcaption>
</figure>

\
\* Equal contribution

# Awards
{{< details "Finalist for the Meta Research PhD Fellowship, 2023" >}}
The Meta Research PhD Fellowship program awards PhD candidates conducting research on the cusp of emerging topics across computer science, engineering, and behavioral science. To support their commitment to furthering research in some of Meta’s key interest areas, Fellows receive full coverage of tuition and university fees for up to two academic years, as well as a $42,000 stipend.

Over 3200 applicants, **62 finalists (top 2%)**, and 17 award winners (top 0.5%).

https://research.facebook.com/blog/2023/4/announcing-the-2023-meta-research-phd-fellowship-award-winners/
{{< /details >}}

{{< details "Vector Scholarship in Artificial Intelligence Recipient, 2020-21" >}}
The Vector Scholarship in Artificial Intelligence supports the recruitment of top students to AI-related master’s programs in Ontario. Valued at $17,500 for one year of full-time study at an Ontario university, these merit-based entrance awards recognize exceptional candidates pursuing a master’s program recognized by the Vector Institute or who are following an individualized study path that is demonstrably AI-focused.

https://vectorinstitute.ai/aimasters
{{< /details >}}

{{< details "NSERC Applied Research Rapid Response to COVID-19 Grant, 2020" >}}
Our project titled "Canadian Hospital Simulator For Management of COVID19 Cases and Contact Tracing" was awarded \$75,000.00.

https://www.nserc-crsng.gc.ca/Innovate-Innover/CCI-COVID_eng.asp
{{< /details >}}

{{< details "Virtual Design Challenge Winner, 2019" >}}
Won 1st place at the VDC hosted by The University of British Columbia with my paper [Proof of Novelty](https://doi.org/10.6084/m9.figshare.10324883.v1). Received a cash prize of $ 3,000.00.

https://blockchain.ubc.ca/virtual-design-challenge-authenticating-and-protecting-full-motion-videos
{{< /details >}}

{{< details "Student Merit Award & Medal, 2015" >}}
Graduated with the highest GPA ever obtained (at the time) for my major. Elected ”Best Student” by the faculty of Electrical & Electronics Engineering at the Federal University of Santa Catarina
{{< /details >}}

{{< details "Science Without Borders Scholarship, 2013" >}}
Awarded a full scholarship that covered tuition, transportation, necessary materials and living costs to study 2 academic semesters at the University of Toronto.
{{< /details >}}

# Talks and Media
- IT@UofT [Source Coding with Latent Variable Models](https://itatuoft.wordpress.com/2021/05/05/source-coding-with-latent-variable-models/), 2021
- [Two ECE grad students receive Vector Institute Scholarships in AI.](https://www.ece.utoronto.ca/news/two-ece-grad-students-receive-vector-institute-scholarships-in-ai/), 2020
- Commit 77338d2 [Pursuing a Career in Data Science](https://anchor.fm/codenationdev/episodes/77338d2---Seguindo-carreira-em-Data-Science-eal947) (pt-BR), 2020
- Hipsters \#106 [Cool Data Science Cases](https://hipsters.tech/casos-bacanas-de-data-science-hipsters-106/) (pt-BR), 2018
---

You may reach me at <img src="email.png" style="display: block; max-width: 350px; width: auto; height: auto">
</img>
