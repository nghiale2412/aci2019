from os import path
import yaml
from kubernetes import client, config


def main():
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    config.load_kube_config()
    k8s_beta = client.ExtensionsV1beta1Api()
    api_instance = client.CoreV1Api()

    with open(path.join(path.dirname(__file__), "deployment.yaml")) as f:
        dep = yaml.load(f)
        resp = k8s_beta.create_namespaced_deployment(
            body=dep, namespace="default")
        print("Deployment created. status='%s'" % str(resp.status))

    with open(path.join(path.dirname(__file__), "service.yaml")) as f1:
        ser = yaml.load(f1)
        resp = api_instance.create_namespaced_service(namespace="default",body=ser,pretty='true')
        print("Service created. status='%s'" % str(resp.status))


if __name__ == '__main__':
main()