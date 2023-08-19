# Tutorial to build a local producer and consumer for tracking events 

This Python project demonstrates generating, producing, and consuming tracking events using Kafka and Avro serialization by Confluent. It consists of code snippets that simulate event data, serialize it using Avro, and then produce and consume events using the Python client packages from Confluent. The code can be executed within a Jupyter Notebook in a virtual environment.

## Prerequisites

- Python 3.6 or higher
- Virtual environment tool (e.g., `venv` or `virtualenv`)
- Jupyter Notebook

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/simonrbtech/tut_local_producer_consumer.git
    cd tut_local_producer_consumer
    ```

2. Create a virtual environment:

    ```bash
    virtualenv venv -p python3
    ```

3. Activate the virtual environment:

    - On macOS and Linux:

    ```bash
    source venv/bin/activate
    ```

    - On Windows:

    ```bash
    .\venv\Scripts\activate
    ```

4. Install project dependencies from `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

5. Install the virtual environment kernel for Jupyter Notebook:

    ```bash
    python -m ipykernel install --user --name=venv 
    ```

Optionally you can run all commands in one go:

```bash
virtualenv venv -p python3 && source venv/bin/activate && pip install -r requirements.txt && python -m ipykernel install --user --name=venv 
```

## Usage

1. Launch Jupyter Notebook:

    ```bash
    jupyter notebook
    ```

2. Open the `tracking_events_notebook.ipynb` notebook in Jupyter.

3. Make sure that `venv` is chosen as the kernel for the notebook. 

4. In the notebook, execute each cell to run the code and observe the results. You can run the code snippets provided in the notebook to generate, produce, and consume tracking events using Kafka and Avro serialization.

5. Remember to stop the notebook kernel when you're done:

    - In the Jupyter Notebook interface, select "Kernel" > "Shutdown."

6. Deactivate the virtual environment when you're finished:

    ```bash
    deactivate
    ```

## License

This project is licensed under the MIT License. For details, please refer to the [LICENSE](LICENSE) file.

The MIT License is a permissive open-source license that allows you to use, modify, and distribute this code for both personal and commercial purposes. It's a common choice for open-source projects due to its simplicity and flexibility.

For the full text of the MIT License, you can visit the official [MIT License page](https://opensource.org/licenses/MIT).
