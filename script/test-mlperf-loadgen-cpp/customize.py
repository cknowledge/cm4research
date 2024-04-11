from cmind import utils
import os

def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    script_path = i['run_script_input']['path']
    src_path = os.path.join(script_path, "src")
    include_path = os.path.join(src_path, 'inc')
    output_path = os.path.join(script_path, "output")

    env["CM_SOURCE_FOLDER_PATH"] = script_path
    env['CM_CXX_SOURCE_FILES'] = "main.cpp"
    env['CM_SOURCE_FOLDER_PATH'] = src_path

    env['CM_LINKER_LANG'] = 'CXX'

    if 'CM_RUN_DIR' not in env:
        env['CM_RUN_DIR'] = output_path

    if not os.path.isdir(env['CM_RUN_DIR']):
        os.makedirs(env['CM_RUN_DIR'])

    for k in ['LDCXXFLAGS', 'CXXFLAGS', 'LFCXXFLAGS', 'CPLUS_INCLUDE_PATH', 'C_INCLUDE_PATH']:
        kk = '+ '+k
        if kk not in env:
            env[kk] = []

    env['+CPLUS_INCLUDE_PATH'].append(include_path)
    env['+C_INCLUDE_PATH'].append(include_path)

    if os_info['platform'] == 'windows':
        env['CM_BIN_NAME']='test-loadgen.exe'
        env['+ LDCXXFLAGS'] += [
          env['CM_MLPERF_INFERENCE_LOADGEN_LIBRARY_PATH']+'\\mlperf_loadgen.lib'
        ]
    else:
        env['CM_BIN_NAME']='test-loadgen'
        env['+ CXXFLAGS'].append("-std=c++14")
        env['+ LDCXXFLAGS'] += [
           "-lmlperf_loadgen",
           "-lpthread",
           "-lm"
        ]


    return {'return':0}


def postprocess(i):

    env = i['env']
    state = i['state']

    return {'return':0}
