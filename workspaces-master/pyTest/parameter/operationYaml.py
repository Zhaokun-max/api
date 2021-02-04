import yaml


def readYaml():
    with open('login.yaml','r',encoding='utf-8') as f:
        return list(yaml.safe_load_all(f))

# for item in readYaml():
#     print(item)