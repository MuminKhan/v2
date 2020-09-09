import argparse
import boto3
import paho.mqtt.client as mqtt

from datetime import datetime


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--server', '--mqtt_server', '-s', 
                        action='store',
                        dest='MQTT_SERVER',
                        default='mqtt')
    parser.add_argument('--port', '--mqtt_port', '-p', 
                        action='store',
                        dest='MQTT_PORT',
                        default=1883)
    parser.add_argument('--topic', '--mqtt_topic', '-t', 
                        action='store',
                        dest='MQTT_TOPIC',
                        default='facey')
    parser.add_argument('--s3-bucket', 
                        action='store',
                        dest='S3_BUCKET',
                        default='w251-hw3')
    parser.add_argument('--s3-key', 
                        action='store',
                        dest='S3_KEY',
                        default='facey')

    arguments = parser.parse_args()
    arguments.MQTT_PORT = int(arguments.MQTT_PORT)

    print("Supplied args:")
    [print(k,v) for k,v in arguments.__dict__.items()]

    return arguments


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(args.MQTT_TOPIC)


def on_message(client, userdata, msg):
    cur_time = datetime.now().strftime("%m_%d_%Y-%H_%M_%S")
    out_file = f'{cur_time}.png'
    msg = bytes(msg.payload)
    response = s3.put_object( 
        Bucket=args.S3_BUCKET,
        Body=msg,
        Key=f'{args.S3_KEY}/{out_file}'
    )
    print(f'Response:{response}')
    

if __name__ == "__main__":
    args = parse_arguments()
    s3 = boto3.client('s3')

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(args.MQTT_SERVER, args.MQTT_PORT, 60)
    client.loop_forever()
