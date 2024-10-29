# Armada Metaflow Extension 

## Introduction

This extension provides a flow decorator: `@armada`, which executes the step
as an [Armada](https://github.com/armadaproject/armada) job.

## Installation

From PyPI (Not yet available as of this writing!):

`pip install armada-metaflow` 

Or clone this repo and install locally:

```bash
$ git clone https://github.com/armadaproject/armada-metaflow
$ cd armada-metaflow
$ pip install .
```

## The @armada Decorator

The `@armada` decorator is relatively simple and straight-forward in purpose: The `@step` method within a Metaflow flow 
decorated by it will be executed as a job launched by Armada. Since Armada is primarily a manager of many kubernetes 
clusters, the end result is similar to the `@kubernetes` decorator. Ultimately the step will execute inside a 
container managed by a kubernetes cluster, which in turn is managed by Armada.

### Required Arguments
Some arguments to the `@armada` decorated are required:
* `host` - The Armada host.
* `port` - The Armada port.
* `queue` - The Armada queue to which the Armada job created by this step will be submitted. Earlier in this how-to we created a queue named `metaflow`.
* `job_set_id` - A way to group related jobs within Armada. The specified job set will be created if it doesn't already exist.
### Live Logs
If you want to have live logs streamed during your flow, then you should specify the following:
* `logging_host` - The logging host, usually Armada's Binoculars service.
* `logging_port` - The logging port, usually Armada's Binoculars service.
>[!WARNING]
>Binoculars is not an officially supported external Armada API or service. It may change or disappear at any time. However
>the `JobLogClient` located in the Python `armada-client` library is meant to be a durable, externally consumable interface 
>for retrieving Armada job logs.

### Optional Arguments
* `cpu` - The requested amount of cpu resources to provide to the Armada job.
* `memory` - The requested amount of memory resource to provide to the Armada job.
* `disk` - The requested amount of disk resource to provide to the Armada job.
* `insecure_no_ssl` - Connections to Armada will not use SSL. Useful for test environments.

## Development / Contributing

Please see the [developer documentation](https://github.com/armadaproject/armada-metaflow/blob/main/docs/Developer.md) 
to learn how to get started on contributing to this project.
