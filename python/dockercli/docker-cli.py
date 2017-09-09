#!/usr/bin/env python3.4

import docker
import argparse
from datetime import datetime

def logando(mensagem, e = None, logfile="docker-cli.log"):
    date_atual = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    with open(logfile,mode='a') as log:
        texto = "%s \t %s " % (date_atual, mensagem)
        if e is not None:
            texto += "\t %s" % (str(e))

        texto += "\n"
        print(texto)
        log.write(texto)


def criar_containers(args):
    client = docker.from_env()
    try:
        executando = client.containers.run(args.imagem,args.comando)
        print(executando)
    except docker.errors.ImageNotFound as e:
        logando("Essa imagem não existe",e)
    except docker.errors.NotFound as e:
        logando('Esse comando não existe', e)
    except Exception as e:
        logando('Deu erro generico',e)
    finally:
        logando('comando executado')

def listar_containers():
    client = docker.from_env()
    get_all = client.containers.list(all)
    for container in get_all:
        conectando = client.containers.get(container.id)
        logando("O conatiner %s utiliza a imagem %s rodando o comando %s"
              % (conectando.short_id,conectando.attrs['Config']['Image'],conectando.attrs['Config']['Cmd']))

def procurar_container(imagem):
    client = docker.from_env()
    get_all = client.containers.list()
    for container in filter(lambda c: client.containers.get(c.id).attrs['Config']['Image'] == imagem,get_all):
        conectando = client.containers.get(container.id)
        logando("O conatiner %s utiliza a imagem %s rodando o comando %s"
              % (conectando.short_id, conectando.attrs['Config']['Image'], conectando.attrs['Config']['Cmd']))
def removercontainer():
    client = docker.from_env()
    get_all = client.containers.list()
    for container in get_all:
        conectando = client.containers.get(container.id)
        for binding in list(conectando.attrs['HostConfig']['PortBindings'].values()):
            porta = int(binding[0]['HostPort'])
            logando("container %s rodando na porta %s" %(conectando.short_id,porta))
            if(porta < 1025):
                containerRemovido = conectando.short_id
                conectando.remove(force=True)
                logando(">>>Container %s removido" % (containerRemovido))

try:
    parser = argparse.ArgumentParser(description="docker cli criado na aula de python")
    subparser = parser.add_subparsers()
    criar_opt = subparser.add_parser('criar')
    criar_opt.add_argument('--imagem',required=True)
    criar_opt.add_argument('--comando',required=True)
    criar_opt.set_defaults(func=criar_containers)

    cmd = parser.parse_args()
    cmd.func(cmd)
except Exception as e:
    logando("Deu erro no comando", e)

#procurar_container("nginx")
#removercontainer()
#criar_containers("alpine","echo vaai")
#listar_containers()