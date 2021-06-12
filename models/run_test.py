import os

models = ['circle','ellipse','raindrop','mix']
datasets = ['circle','ellipse','raindrop','mix']

for model in models:
    for data in datasets:
        os.system('python test.py --weights ./runs/train/%s/weights/best.pt --data ./data/%s.yaml --task val --img 640 --device 2,3 --name %s2%s --conf 0.65 --iou 0.5' % (model,data,model,data))