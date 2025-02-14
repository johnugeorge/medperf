# Instructions for Data Providers

## Preparing a Dataset 

Once your registration is approved, you can prepare a raw dataset to be used in a benchmark following the steps below:

1. Use the following command to start the data preparation process, where <code>path/<strong>to</strong>/labels</code> is the specific path to the dataset labels, <code>benchmark_uid</code> is the unique identifier of the benchmark you want to associate to,  <code>dataset_name</code> is the name you want to give to the dataset, <code>dataset_description</code> can be used to describe it, and <code>dataset_location</code> is origin of the dataset (e.g. organization name).

```
medperf dataset create -b <benchmark_uid> -d <path/to/data> -l <path/to/labels> --name <dataset_name> --description <dataset_description> --location <dataset_location>
```

If the request is successful, the CLI will return a response as follows:

```
MedPerf 0.0.0
Benchmark Data Preparation: xrv
> Preparation cube download complete
> MLCommons TorchXRayVision Preprocessor MD5 hash check complete
> Cube execution complete
> Sanity checks complete
> Statistics complete
✅ Done!
Next step: register the dataset with 'medperf dataset submit -d <generated_uid>'
```

2. The next step is to submit the dataset with the following command:

```
medperf dataset submit -d <generated_uid>
```

The CLI will return a response as follows: 

```
MedPerf 0.0.0

====================
data_preparation_mlcube: '1'
description: name
generated_uid: 63a58fa902e131c2f0c3d8e8ca6498dc5a706504
input_data_hash: b7248606e46fd2ab31d69bbac9d65ffedbeb0b1b
location: test
metadata:
  column statistics:
    Atelectasis:
      '0.0': 0.625
      '1.0': 0.375
    Cardiomegaly:
      '0.0': 0.67
      '1.0': 0.33
    Consolidation:
      '0.0': 0.84
      '1.0': 0.16
    Edema:
      '0.0': 0.79
      '1.0': 0.21
  images statistics:
    channels: 1
    height:
      max: 224.0
      mean: 224.0
      min: 224.0
      std: 0.0
    pixels_max:
      max: 255.0
      mean: 255.0
      min: 255.0
      std: 0.0
    pixels_mean:
      max: 149.2486049107
      mean: 137.7983645568
      min: 121.2493223852
      std: 5.8131783153
    pixels_min:
      max: 6.0
      mean: 0.07
      min: 0.0
      std: 0.5063416925
    pixels_std:
      max: 79.0369075709
      mean: 71.5894559861
      min: 64.0834766712
      std: 2.8957115261
    width:
      max: 224.0
      mean: 224.0
      min: 224.0
      std: 0.0
  labels:
  - Atelectasis
  - Cardiomegaly
  - Consolidation
  - Edema
  size: 200
name: test
separate_labels: false
split_seed: 0
state: OPERATION
status: PENDING
====================

Above are the information and statistics that will be registered to the database
Do you approve the registration of the presented data to the MLCommons comms? [Y/n] Y
Uploading...
✅ Done!
Next step: associate the dataset with 'medperf dataset associate -b <BENCHMARK_UID> -d <generated_uid>'
```

3. After running the submit command successfully, note that the CLI will ask you if you want to confirm the dataset registration to the MLCommons database. Send Y to confirm or N to halt the process.

**Note:** The submission of a dataset is not the same as its upload. The data stays in the user’s machine and we only upload metadata regarding the dataset, which must be approved beforehand by the user.

4. Finally, you need to associate the dataset to the benchmark using the following command:

```
medperf dataset associate -b <BENCHMARK_UID> -d <generated_uid>
```

The CLI will return a response as follows:

```
MedPerf 0.0.0
Benchmark Execution: tmp_1_2_3
> Metrics cube download complete
> xrv_metrics MD5 hash check complete
> Model cube download complete
> xrv_chex_densenet MD5 hash check complete
> Model execution complete
These are the results generated by the compatibility test. 
This will be sent along the association request.
They will not be part of the benchmark.

====================
approval_status: PENDING
benchmark: tmp_1_2_3
dataset: 1
metadata: {}
model: 2
name: tmp_1_2_3_2_1
results:
  AUC:
    Atelectasis: 0.8024533333333334
    Cardiomegaly: 0.7913839891451833
    Consolidation: 0.8694196428571428
    Edema: 0.8300180831826401
  F1:
    Atelectasis: 0.6379310344827586
    Cardiomegaly: 0.6243386243386244
    Consolidation: 0.378698224852071
    Edema: 0.422680412371134
====================

Please confirm that you would like to associate the dataset test with the benchmark xrv. [Y/n] Y
Generating dataset benchmark association
✅ Done!
Next step: Once approved, run the benchmark with 'medperf run -b <benchmark_uid> -d <generated_uid>
```

5. Confirm whether you would like to associate the dataset with the benchmark. 
6. After the submission and association of the dataset, you need to wait for the Benchmark Committee to approve your request. 

### Obtaining information from a dataset 

The following command will give you more information about the dataset, such as registration status and, most importantly, the unique identifier (UID) of the dataset, which will then be used as<code> <strong>&lt;dataset_uid></strong></code>: 

```
medperf dataset ls
```

A response examples from the CLI for that command is shown as follows:

```
MedPerf 0.0.0
UID      Server UID  Name  Data Preparation Cube UID  Registered    Local
—-----   —---------  —---  —------------------------  —---------    —-----
<uid>                test                          1   False        True
```

## Running an Experiment 

After the Benchmark Committee approves your dataset submission and association, you can start experimenting. 

There are basically two methods for generating and submitting results:

1. [Creating an experiment](#creating-an-experiment) and then submitting the results separately;
2. Using the run command to [create and submit results with just a command](#creating-an-experiment-and-submitting-results-with-a-single-command).

**Note:** Both the dataset and the model must have been approved by the benchmark owner.

### Creating an Experiment 

You can obtain metrics for a given benchmark, dataset and model with the following command:

```
medperf result create -b <benchmark_uid> -d <dataset_uid> -m <model_uid>
```

Then CLI will provide a response as follows:

```
MedPerf 0.0.0
Benchmark Execution: xrv
> Metrics cube download complete
> MLCommons Metrics MD5 hash check complete
> Model cube download complete
> MLCommons TorchXRayVision CheXpert DenseNet model MD5 hash check complete
> Model execution complete
✅ Done!
```

### Submitting results

This command will submit the results under the user’s approval. If submissions are canceled by the user, it can always be done again with:

```
medperf result submit -b <benchmark_uid> -d <dataset_uid> -m <model_uid>
```

Then CLI will provide a response as follows:

```
MedPerf 0.0.0

====================
approval_status: PENDING
benchmark: 1
dataset: 1
metadata: {}
model: 2
name: '1_2_1'
results:
  AUC:
    Atelectasis: 0.8024533333333334
    Cardiomegaly: 0.7913839891451833
    Consolidation: 0.8694196428571428
    Edema: 0.8300180831826401
  F1:
    Atelectasis: 0.6379310344827586
    Cardiomegaly: 0.6243386243386244
    Consolidation: 0.378698224852071
    Edema: 0.422680412371134
====================

Above are the results generated by the model
Do you approve uploading the presented results to the MLCommons comms? [Y/n] Y
✅ Done!
```

After that, you need to whether approve (Y) or not (n) the submission of the results.

### Creating an experiment and submitting results with a Single Command 

 You can create results and submit them with the following command: 

```
medperf run -b <benchmark_uid> -d <generated_uid> -m <model_uid>
```

Then CLI will provide a response as follows:

```
MedPerf 0.0.0
Benchmark Execution: xrv
> Metrics cube download complete
> MLCommons Metrics MD5 hash check complete
> Model cube download complete
> MLCommons TorchXRayVision CheXpert DenseNet model MD5 hash check complete
> Model execution complete

====================
approval_status: PENDING
benchmark: 1
dataset: 1
metadata: {}
model: 2
name: '1_2_1'
results:
  AUC:
    Atelectasis: 0.8024533333333334
    Cardiomegaly: 0.7913839891451833
    Consolidation: 0.8694196428571428
    Edema: 0.8300180831826401
  F1:
    Atelectasis: 0.6379310344827586
    Cardiomegaly: 0.6243386243386244
    Consolidation: 0.378698224852071
    Edema: 0.422680412371134
====================

Above are the results generated by the model
Do you approve uploading the presented results to the MLCommons comms? [Y/n] Y
✅ Done!
```

After that, you need to whether approve (Y) or not (n) the submission of the results. 

### Getting information about your results 

In addition, you can get information about your results with:

```
medperf result ls
```

The CLI will return a response such as:

```
MedPerf 0.0.0
Benchmark UID      Model UID    Data UID  Submitted    Local
---------------  -----------  ----------  -----------  -------
1                          2           1  True         True
tmp_1_2_3                  2           1  False        True
```

