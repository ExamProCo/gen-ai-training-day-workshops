# AWS Setup

## Install AWS CLI

We don't directly need the AWS CLI but its useful to have around for debugging or quickly creating on off resources like an S3 Bucket

```sh
chmod u+x ./bin/install_aws_cli
./bin/install_aws_cli
```

> SageMaker StudioLabs JuypterLabs Workspace will have AWS CLI preinstalled

## Configure your AWS Credentials

You can set your AWS Credentials two ways:
- Env Vars
- AWS Credentials Profile


Cloud developer enviroments will require you set env vars since they can't persist or store an `~/.aws/credentaisls` file:

```sh
export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""
export AWS_DEFAULT_REGION="ca-central-1"
```

> Note that LLM offerings vary per region so you may need to change the AWS_DEFAULT_REGION to whatever works best for you.

Local developer enviroments you can use AWS configure which will persist or store credentials in a `~/.aws/credentaisls` file:

```sh
aws configure
```

> Please consider there can be limitations of models or features based on selected region. In worst-case we will fallback to nearest best suppported region>

> SageMaker StudioLabs JuypterLabs Workspace will use your user roll for permissions so you don't need to set credentinals