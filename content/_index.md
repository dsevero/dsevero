---
title: About me
type: docs
---
<img src="http://2.gravatar.com/avatar/5f4137714834378cbeb267932bb101c3?s=200" style="border-radius: 15%; float: left; padding-right: 15px ">
I'm a graduate student at the <a href="https://www.ece.utoronto.ca/">University of Toronto</a> and <a href="https://vectorinstitute.ai/">Vector Institute for Artificial Intelligence</a> researching Machine Learning and Information Theory with my advisors <a href="https://www.ece.utoronto.ca/people/khisti-a/">Ashish Khisti</a> and <a href="http://www.alireza.ai/">Alireza Makhzani</a>. I have a B.Sc. in Electronics Engineering from the Federal University of Santa Catarina (Brazil) where I was advised by <a href="http://danilosilva.sites.ufsc.br/">Danilo Silva</a>. Previously, I was an engineer at <a href="https://research.3778.care/">37.78</a> working with Machine Learning for healthcare.

My research interests include the Minimum Description Length (MDL) Principle and its connections to machine learning and data compression. I am Currently working on lossless compression through bits-back coding and deep latent variable models.

Originally, I am from Florianópolis, Brazil but I've lived in New Jersey, Orlando, Toronto and São Paulo as well as other smaller cities in the south of Brazil. I enjoy reading, playing american football and <a href="https://www.kerbalspaceprogram.com/">KSP</a>.

---
# News
{{< hint info >}}
**16/Oct/2020** I've joined the Vector Institute as a graduate student researcher.
{{< /hint >}}
- **14/May/2020** I am a Vector Scholarship in Artificial Intelligence Recipient 2020-21.
- **27/Feb/2020** Starting graduate studies at University of Toronto in Fall/2020.
- **03/Dec/2019** Proof of Novelty was awarded by [Blockchain@UBC](https://blockchain.ubc.ca/news/virtual-design-challenge-authenticating-and-protecting-full-motion-videos).
- **15/Nov/2019** Finished writing [Proof of Novelty](https://github.com/dsevero/Proof-of-Novelty).
- **21/Oct/2019** Preprint of [Ward2ICU](https://arxiv.org/abs/1910.00752) posted on arXiv.
- **02/Oct/2019** This page was created.

# Publications
{{< details "Predicting Multiple ICD-10 Codes from Brazilian-Portuguese Clinical Notes (BRACIS 2020)" >}}
Arthur D Reys, Danilo Silva, **Daniel Severo**, Saulo Pedro, Marcia M Sá, Guilherme AC Salgado

https://arxiv.org/abs/2008.01515

ICD coding from electronic clinical records is a manual, time-consuming and expensive process. Code assignment is, however, an important task for billing purposes and database organization. While many works have studied the problem of automated ICD coding from free text using machine learning techniques, most use records in the English language, especially from the MIMIC-III public dataset. This work presents results for a dataset with Brazilian Portuguese clinical notes. We develop and optimize a Logistic Regression model, a Convolutional Neural Network (CNN), a Gated Recurrent Unit Neural Network and a CNN with Attention (CNN-Att) for prediction of diagnosis ICD codes. We also report our results for the MIMIC-III dataset, which outperform previous work among models of the same families, as well as the state of the art. Compared to MIMIC-III, the Brazilian Portuguese dataset contains far fewer words per document, when only discharge summaries are used. We experiment concatenating additional documents available in this dataset, achieving a great boost in performance. The CNN-Att model achieves the best results on both datasets, with micro-averaged F1 score of 0.537 on MIMIC-III and 0.485 on our dataset with additional documents.
{{< /details >}}


# Preprints
{{< details "Proof of Novelty" >}}
Daniel Severo

https://doi.org/10.6084/m9.figshare.10324883.v1

We propose a design for securing novelty of archived content in distributed ledgers, called Proof of Novelty. What constitutes as novel is decided through a consensus mechanism together with a similarity function, which is selected according to the content type (e.g. full-motion videos, textual documents). Scalability is guaranteed by forming a validation committee with cryptographic sortition, which use statistical hypothesis testing to decide on the probability of a content being novel or not. The system can trade-off computational with statistical performance by manipulating parameters. We discuss the usage of this design to secure the novelty of full-motion videos and end with a proposal of future lines of research that can extend the systems capabilities.
{{< /details >}}
{{< details "Ward2ICU: A Vital Signs Dataset of Inpatients from the General Ward" >}}
**Daniel Severo**, Flávio Amaro, Estevam R Hruschka Jr, André Soares de Moura Costa

https://arxiv.org/abs/1910.00752

We present a proxy dataset of vital signs with class labels indicating patient transitions from the ward to intensive care units called Ward2ICU. Patient privacy is protected using a Wasserstein Generative Adversarial Network to implicitly learn an approximation of the data distribution, allowing us to sample synthetic data. The quality of data generation is assessed directly on the binary classification task by comparing specificity and sensitivity of an LSTM classifier on proxy and original datasets. We initialize a discussion of unintentionally disclosing commercial sensitive information and propose a solution for a special case through class label balancing

{{< /details >}}
{{< details "A Report on the Ziggurat Method" >}}
Daniel Severo

https://doi.org/10.6084/m9.figshare.10324868.v1

This report outlines, as well as provides a mathematical proof of functionality, of a highly efficient pseudo-random number generator: The Ziggurat Method. A simple ready-to-use code has been provided by previous authors. We contribute to this with a speed test on a modern Intel processor, as well as a Python script that generates all the necessary information to implement a specific version of the algorithm.
{{< /details >}}

# Awards
{{< details "Vector Scholarship in Artificial Intelligence Recipient 2020-21" >}}
The Vector Scholarship in Artificial Intelligence supports the recruitment of top students to AI-related master’s programs in Ontario. Valued at $17,500 for one year of full-time study at an Ontario university, these merit-based entrance awards recognize exceptional candidates pursuing a master’s program recognized by the Vector Institute or who are following an individualized study path that is demonstrably AI-focused.

https://vectorinstitute.ai/aimasters
{{< /details >}}

{{< details "NSERC Applied Research Rapid Response to COVID-19 Grant" >}}
Our project titled "Canadian Hospital Simulator For Management of COVID19 Cases and Contact Tracing" was awarded \$75,000.00.

https://www.nserc-crsng.gc.ca/Innovate-Innover/CCI-COVID_eng.asp
{{< /details >}}

{{< details "Virtual Design Challenge Winner 2019" >}}
Won 1st place at the VDC hosted by The University of British Columbia with my paper Proof of Novelty. Received a cash prize of $ 3,000.00.

https://blockchain.ubc.ca/virtual-design-challenge-authenticating-and-protecting-full-motion-videos
{{< /details >}}

{{< details "Student Merit Award & Medal 2015" >}}
Graduated with the highest GPA ever obtained (at the time) for my major. Elected ”Best Student” by the faculty of Electrical & Electronics Engineering at the Federal University of Santa Catarina
{{< /details >}}

{{< details "Science Without Borders Scholarship 2013" >}}
Awarded a full scholarship that covered tuition, transportation, necessary materials and living costs to study 2 academic semesters at the University of Toronto.
{{< /details >}}

# Talks and Media
- [Two ECE grad students receive Vector Institute Scholarships in AI.](https://www.ece.utoronto.ca/news/two-ece-grad-students-receive-vector-institute-scholarships-in-ai/)
- Commit 77338d2 [Pursuing a Career in Data Science](https://anchor.fm/codenationdev/episodes/77338d2---Seguindo-carreira-em-Data-Science-eal947) (pt-BR)
- Hipsters \#106 [Cool Data Science Cases](https://hipsters.tech/casos-bacanas-de-data-science-hipsters-106/) (pt-BR)
---

You may reach me at <img src="email.png" style="display: block; max-width: 350px; width: auto; height: auto">
</img>
