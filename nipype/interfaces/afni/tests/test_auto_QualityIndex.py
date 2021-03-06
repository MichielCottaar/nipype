# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..preprocess import QualityIndex


def test_QualityIndex_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    autoclip=dict(argstr='-autoclip',
    usedefault=True,
    xor=['mask'],
    ),
    automask=dict(argstr='-automask',
    usedefault=True,
    xor=['mask'],
    ),
    clip=dict(argstr='-clip %f',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='%s',
    mandatory=True,
    position=-2,
    ),
    interval=dict(argstr='-range',
    usedefault=True,
    ),
    mask=dict(argstr='-mask %s',
    xor=['autoclip', 'automask'],
    ),
    out_file=dict(argstr='> %s',
    keep_extension=False,
    name_source=['in_file'],
    name_template='%s_tqual',
    position=-1,
    ),
    quadrant=dict(argstr='-quadrant',
    usedefault=True,
    ),
    spearman=dict(argstr='-spearman',
    usedefault=True,
    ),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    )
    inputs = QualityIndex.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_QualityIndex_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = QualityIndex.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
