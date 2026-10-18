# Create an RouterOS CHR 7.6 AMI

> Source: https://help.mikrotik.com/docs/spaces/RKB/pages/161611810/Create+an+RouterOS+CHR+7.6+AMI
>
> Only on help.mikrotik.com: the manual has no equivalent page. The help site is frozen; this page was last edited 2022-12-15.

Prior to using this procedure, you will need to have a properly set up AWS CLI environment that has permissions (IAM Roles) allowing for VM importing and access to your S3 bucket. Here's [Amazon's documentation](https://docs.aws.amazon.com/vm-import/latest/userguide/required-permissions.html) for adding the permissions and roles.

## Step-by-step guide

1. Make sure you have a properly configured AWS CLI environment.
2. Download the CHR 7.6 Raw disk image from the [Mikrotik Downloads](https://mikrotik.com/download) page.
3. Upload the chr-7.6.img file to an S3 bucket.
4. Create the two files shown below.
5. Update your S3Bucket and S3Key in the JSON file.
6. Run the following command: "bash aws-import-snapshot-mikrotik-chr-76.sh import-snapshot"
7. Grab the value of **ImportTaskId** from the output of the last command.
8. Run the following command: "bash aws-import-snapshot-mikrotik-chr-76.sh monitor-import [**ImportTaskId**]" with the **ImportTaskId** as the last argument.
9. Wait until the Status shows complete, at which time you can press CTRL-C to break the script.
10. Grab the value of **SnapshotId** from the output.
11. Run the following command: "bash aws-import-snapshot-mikrotik-chr-76.sh register-image [**SnapshotId**]" with the **SnapshotId** as the last argument.
12. Grab the value of **ImageId** from the output of the last command. If everything was successful, this is the ID of your AMI.
13. Go to the AWS control panel for EC2 -> Images -> AMIs to find your new Amazon Machine Image. You can now use it to **Launch instance from AMI**.

## mikrotik-routeros-chr-76-raw-containers.json

> **Info**
>
> {
>   "Description": "Mikrotik RouterOS CHR v7.6 RAW",
>   "Format": "raw",
>   "UserBucket": {
>     "S3Bucket": "my-s3-bucket",
>     "S3Key": "mikrotik/chr-7.6.img"
>   }
> }

## aws-import-snapshot-mikrotik-chr-76.sh

> **Info**
>
> #!/bin/bash
>
> description="Mikrotik RouterOS CHR v7.6"
> json_file="mikrotik-routeros-chr-76-raw-containers.json"
>
> JOB="$1"
>
> case $JOB in
>     "import-snapshot")
>         aws ec2 import-snapshot --description "${description} image" --disk-container file://${json_file}
>         ;;
>
>     "monitor-import")
>         import_task_id="$2"
>
>         while true; do
>             clear
>             date
>             echo ""
>             aws ec2 describe-import-snapshot-tasks --import-task-ids ${import_task_id}
>             sleep 10
>         done
>
>         #
>         #snapshot_id=$(aws ec2 describe-import-snapshot-tasks --import-task-ids ${import_task_id} | grep SnapshotId | awk -F '"'  '{print $4}')
>         #
>         ;;
>
>     "register-image")
>         snapshot_id="$2"
>
>         aws ec2 register-image \
>           --name "$description" \
>           --description "$description" \
>           --architecture x86_64 \
>           --virtualization-type hvm \
>           --ena-support \
>           --root-device-name "/dev/sda1" \
>           --block-device-mappings "[{\"DeviceName\": \"/dev/sda1\", \"Ebs\": { \"SnapshotId\": \"$snapshot_id\"}}]"
>     ;;
>
>     *)
>         echo "Unknown job type: ${JOB}"
>     ;;
> esac

## Related articles

- [Create an RouterOS CHR 7.6 AMI](https://help.mikrotik.com/docs/spaces/RKB/pages/161611810/Create+an+RouterOS+CHR+7.6+AMI)
