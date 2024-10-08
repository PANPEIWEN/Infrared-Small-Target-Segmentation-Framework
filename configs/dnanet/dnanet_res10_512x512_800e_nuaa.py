_base_ = [
    '../_base_/datasets/nuaa.py',
    '../_base_/default_runtime.py',
    '../_base_/schedules/schedule_500e.py'
]
# model settings
model = dict(
    name='DNANet',
    type='EncoderDecoder',
    pretrained=None,
    backbone=dict(
        type=None,
        type_info='resnet',
    ),
    decode_head=dict(
        type='DNANet',
        num_classes=1,
        input_channels=3,
        block_name='resnet',
        num_blocks=[1, 1, 1, 1],
        nb_filter=[16, 32, 64, 128, 256]
    ),
    loss=dict(type='SoftIoULoss')
)
optimizer = dict(
    type='Adagrad',
    setting=dict(lr=0.05, weight_decay=1e-4)
)
runner = dict(type='EpochBasedRunner', max_epochs=800)
