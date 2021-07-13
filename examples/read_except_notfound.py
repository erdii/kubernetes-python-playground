from os import environ
from kubernetes import client, config

def main():
	kubeconfig_path = environ.get('KUBECONFIG')
	print(f"KUBECONFIG = {kubeconfig_path}")
	config.load_kube_config(config_file=kubeconfig_path)

	k8s_core_v1 = client.CoreV1Api()

	namespace = "default"
	name = "foo"

	try:
		configmap = k8s_core_v1.read_namespaced_config_map(name, namespace)
	except client.rest.ApiException as apiEx:
		if apiEx.reason == 'Not Found':
			print(f"K8s: {namespace}/{name} does not exist")
		else:
			print("lol")
			raise apiEx

main()
