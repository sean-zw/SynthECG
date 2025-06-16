# SynthECG: A Comprehensive Evaluation Framework for Synthetic ECGs

![SynthECG](https://img.shields.io/badge/SynthECG-Ready-brightgreen) ![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![PyTorch](https://img.shields.io/badge/PyTorch-1.7%2B-orange)

Welcome to the **SynthECG** repository! This project offers the first systematic evaluation framework for generating synthetic 10-second 12-lead ECGs using diagnostic class-conditioned generative models. With the rise of deep learning and generative AI, we aim to enhance the field of medical AI, particularly in electrocardiogram (ECG) analysis.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Getting Started](#getting-started)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Evaluation Framework](#evaluation-framework)
7. [Datasets](#datasets)
8. [Contributing](#contributing)
9. [License](#license)
10. [Contact](#contact)
11. [Releases](#releases)

## Introduction

The **SynthECG** project focuses on creating synthetic ECG data that can be used for various applications in medical research and machine learning. By utilizing advanced generative models, we aim to produce high-quality synthetic ECGs that maintain the characteristics of real-world data. This framework allows researchers to evaluate the performance of different models and techniques in generating realistic ECG signals.

## Features

- **Systematic Evaluation**: Provides a structured approach to evaluate synthetic ECGs.
- **Generative Models**: Utilizes GANs and diffusion models for generating synthetic data.
- **Medical Applications**: Focuses on applications in the medical field, particularly in cardiology.
- **Open Source**: Fully open-source and available for contributions.
- **Comprehensive Documentation**: Detailed documentation to help users get started quickly.

## Getting Started

To get started with **SynthECG**, you will need to clone the repository and install the required dependencies. Below, you will find detailed instructions to set up the environment.

## Installation

1. **Clone the Repository**

   Use the following command to clone the repository:

   ```bash
   git clone https://github.com/sean-zw/SynthECG.git
   cd SynthECG
   ```

2. **Install Dependencies**

   Ensure you have Python 3.8 or higher installed. You can create a virtual environment and install the required packages:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

## Usage

After installing the dependencies, you can start using the framework to generate synthetic ECGs. The main script for generating ECGs is located in the `src` directory.

### Generating Synthetic ECGs

To generate synthetic ECGs, run the following command:

```bash
python src/generate_ecg.py --model <model_name> --num_samples <number_of_samples>
```

Replace `<model_name>` with the name of the generative model you want to use, and `<number_of_samples>` with the desired number of ECG samples.

## Evaluation Framework

The evaluation framework is designed to assess the quality of synthetic ECGs. It includes various metrics to compare synthetic data against real-world ECGs. Key metrics include:

- **Signal Quality Index (SQI)**: Measures the quality of the ECG signal.
- **Similarity Metrics**: Compares the statistical properties of synthetic and real ECGs.
- **Visual Inspection**: Provides visualizations for qualitative analysis.

### Running Evaluations

To run the evaluation framework, use the following command:

```bash
python src/evaluate_ecg.py --synthetic_dir <path_to_synthetic_data> --real_dir <path_to_real_data>
```

This command will generate evaluation reports and visualizations.

## Datasets

**SynthECG** leverages several datasets for training and evaluation. The primary dataset used is the PTB-XL dataset, which contains a diverse range of ECG recordings.

### PTB-XL Dataset

- **Description**: The PTB-XL dataset includes over 21,000 ECG recordings from more than 18,000 patients.
- **Access**: You can download the dataset from [PTB-XL website](https://physionet.org/static/published-project/ptbxl-1.0.1/).

## Contributing

We welcome contributions to the **SynthECG** project! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

Please ensure that your code follows the style guidelines and is well-documented.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or suggestions, feel free to reach out via the Issues section of this repository or contact the maintainer directly.

## Releases

You can find the latest releases of **SynthECG** [here](https://github.com/sean-zw/SynthECG/releases). Please download the latest version and follow the instructions for installation and usage.

Explore the exciting world of synthetic ECGs with **SynthECG** and contribute to advancing medical AI!

---

For more information and updates, visit our [Releases](https://github.com/sean-zw/SynthECG/releases) section.