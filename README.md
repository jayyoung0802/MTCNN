# Mtcnn
MTCNN tensorflow版本复现源码，在FDDB上测试TPR94.9%，FP不到1300.


		gen_hard_bbox_pnet.py用于产生12*12的训练图片
		gen_hard_bbox_rnet_onet.py用于产生R,O网络所需的24*24，以及48*48的训练图片。
		gen_landmark_aug.py用于产生12*12,24*24,48*48的特征点训练图片
		training.py用于训练P，R，O网络。
		gen_tfrecords.py用于将训练数据保存为tfrecord格式，以便于训练。


####训练步骤：
* PNet

		1、python gen_hard_bbox_pnet.py
		2、python gen_landmark_aug.py --stage pnet
		3、python gen_tfrecords.py --stage pnet
		4、python train.py --stage pnet
* RNet

		5、python gen_hard_bbox_rnet_onet.py --stage rnet
		6、python gen_landmark_aug.py --stage rnet
		7、python gen_tfrecords.py --stage rnet
		8、python train.py --stage rnet
* ONet

		9、python gen_hard_bbox_rnet_onet.py --stage onet
		10、python gen_landmark_aug.py --stage onet
		11、python gen_tfrecords.py --stage onet
		12、python train.py --stage onet
