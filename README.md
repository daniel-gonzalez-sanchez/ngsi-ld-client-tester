# NGSI-LD client tester

Tester for the [`Python-based NGSI-LD API client`](https://github.com/giros-dit/python-ngsi-ld-client/tree/1.6.1) compliant with the [NGSI-LD API OpenAPI specification](https://forge.etsi.org/rep/cim/NGSI-LD/-/tree/1.6.1).

To deploy a docker-compose scenario with the [`Orion-LD`](https://github.com/FIWARE/context.Orion-LD) context broker (a reference implementation of NGSI-LD context broker compliant with the  NGSI-LD API specification by [ETSI GS CIM 009 V1.6.1](https://www.etsi.org/deliver/etsi_gs/CIM/001_099/009/01.06.01_60/gs_CIM009v010601p.pdf)), execute the following command:
```bash
$ docker-compose up
```

In case you are interested in running the scenario in background, use the following command:
```bash
$ docker-compose up -d
```

Tear the scenario down as follows:
```bash
$ docker-compose down
```

> **Note:**
>
> In the `.env` file, environment variables are defined and parameterized (i.e., the context broker endpoint and the NGSI-LD context URL).

Within the [/ngsi-ld-models](ngsi-ld-models/) folder there is a Python library with the [Pydantic](https://docs.pydantic.dev/latest/) class generation for the schemas defined in a custom OpenAPI available [here](ngsi-ld-api-sensor-model.yaml). This custom OpenAPI encompass the `NGSI-LD API V1.6.1` with the native NGSI-LD API metamodel schemas and customizable schemas for a demo NGSI-LD Entity of type `Sensor` used in this NGSI-LD client tester (a sample of JSON payloads for the NGSI-LD Entity of type `Sensor` is available [here](sensor-tester/example/example-normalized.json)).

To validate the [`create_entity`](https://github.com/giros-dit/python-ngsi-ld-client/blob/1.6.1/docs/ContextInformationProvisionApi.md#create_entity), [`retrieve_entity`](https://github.com/giros-dit/python-ngsi-ld-client/blob/1.6.1/docs/ContextInformationConsumptionApi.md#retrieve_entity), [`query_entity`](https://github.com/giros-dit/python-ngsi-ld-client/blob/1.6.1/docs/ContextInformationConsumptionApi.md#query_entity), [`update_entity`](https://github.com/giros-dit/python-ngsi-ld-client/blob/1.6.1/docs/ContextInformationProvisionApi.md#update_entity), and [`delete_entity`](https://github.com/giros-dit/python-ngsi-ld-client/blob/1.6.1/docs/ContextInformationProvisionApi.md#delete_entity) `CRUD` operations for a simple NGSI-LD Entity (e.g., NGSI-LD Entity of type Sensor available [here](sensor-tester/example/example-normalized.json)), follow these steps:
1. Download and install `poetry` by following the [official documentacion](https://python-poetry.org/docs/master/#installing-with-the-official-installer).
2. Make sure you have the right Python version for this project (Python>3.9 in this case):
     ```bash
    $ sudo apt-get install python3.9
    ```
3. Install `distutils` package for your specific Python release:
    ```bash
    $ sudo apt-get install python3-distutils
    ```
4. Install `python-is-python3` package (symlinks /usr/bin/python to Python3 as specified in [link 1](https://askubuntu.com/questions/1296790/python-is-python3-package-in-ubuntu-20-04-what-is-it-and-what-does-it-actually) and [link 2](https://stackoverflow.com/questions/61921940/running-poetry-fails-with-usr-bin-env-python-no-such-file-or-directory)):
    ```bash
    $ sudo apt-get install python-is-python3
    ```
5. To build the `ngsi_ld_models` library with the Python-generated classes for the sample NGSI-LD Entity of type `Sensor`, follow these steps:
    - Move to [`/ngsi-ld-models`](ngsi-ld-models/) folder:
        ```bash
        $ cd sensor-tester
        ```
    - Install the dependencies for the `ngsi_ld_models` library with [Poetry](https://python-poetry.org/):
        ```bash
        $ poetry install
        ```
        The `ngsi_ld_models` Python library is now installed and prepared to be used.
6. To play with the  NGSI-LD API `CRUD` operations for the demo NGSI-LD Entity of type `Sensor`, first follow these preparation steps: 
    - Move to [`/sensor-tester`](sensor-tester/) folder:
        ```bash
        $ cd sensor-tester
        ```
    - Enable virtual environment for your specific Python release:
        ```bash
        $ poetry env use 3.9
        ```
        > **Note:**
        >
        > If you work with [Visual Studio Code (VSC)](https://code.visualstudio.com/) IDE, it is recommendable to open the `/sensor-tester` folder in an independet workspace so that the virtual environment can select the correct Python interpreter and thus recognize the source code well. In VSC you can specify the correct Python interpreter by using the [**Python: Select Interpreter** command](https://code.visualstudio.com/docs/python/environments#_working-with-python-interpreters) from the **Command Palette** (`Ctrl+Shift+P`).
    - Setup the virtual environment with Poetry:
        ```bash
        $ poetry shell
        (sensor-tester-py3.9) $ poetry install
        ```
        The virtual environment is now activated and ready to be used.
7. To create a sample NGSI-LD Entity (e.g, NGSI-LD Entity of type `Sensor`), run the [sensor-tester/create-sensor-entity.py](sensor-tester/create-sensor-entity.py) Python script as follow:
    ```bash
    (sensor-tester-py3.9) $ python create-sensor-entity.py
    ```
8. To retrieve the previously created NGSI-LD Entity by using its `id` field, run the [sensor-tester/retrieve-sensor-entity.py](sensor-tester/retrieve-sensor-entity.py) Python script as follow:
    ```bash
    (sensor-tester-py3.9) $ python retrieve-sensor-entity.py
    ```
9. To query all the NGSI-LD Entities of a particular type (e.g, NGSI-LD Entity of type `Sensor`), run the [sensor-tester/query-sensor-entities.py](sensor-tester/query-sensor-entities.py) Python script as follow:
    ```bash
    (sensor-tester-py3.9) $ python query-sensor-entities.py
    ```
10. To update the previously created NGSI-LD Entity by using its `id` field, run the [sensor-tester/update-sensor-entity.py](sensor-tester/update-sensor-entity.py) Python script as follow:
    ```bash
    (sensor-tester-py3.9) $ python update-sensor-entity.py
    ```
11. To delete the previously created NGSI-LD Entity by using its `id` field, run the [sensor-tester/delete-sensor-entity.py](sensor-tester/delete-sensor-entity.py) Python script as follow:
    ```bash
    (sensor-tester-py3.9) $ python delete-sensor-entity.py
    ```
    
In addition, for validating example JSON-LD payloads (e.g., [`Sensor`](sensor-tester/example/example-normalized.json) example) against the autogenerated Python class bindings (e.g., `Sensor` Pydantic class available [here](ngsi-ld-models/ngsi_ld_models/models/sensor.py)), run the [/sensor-tester/tests/test_sensor.py](sensor-tester/tests/test_sensor.py) Python unit test from the `sensor-tester` folder as follows:
```bash
$ cd sensor-tester
$ poetry shell
(sensor-tester-py3.9) $ python tests/test_sensor.py
```
