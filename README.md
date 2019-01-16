# keras-unet

The goal is to design a segmentation network that can run fairly fast in [TensorflowJS](https://js.tensorflow.org)

Try the [live demo](https://ldenoue.github.io/keras-unet/) in your browser. The regular Conv2D UNet should get you around 5 FPS, while the Separable UNet reached 10 FPS on a 2012 MacBook Air.

The UNets are trained on 3 datasets: HeadShoulderData, PersonData, HumanParsingData. The original UNet comes from https://github.com/Golbstein/Fingernails-Segmentation who applied it to segmenting fingernails.

The datasets are from:
- "PersonData" [Unet-for-Person-Segmentation](https://github.com/TianzhongSong/Unet-for-Person-Segmentation)
- "HumanParsingData" [Person-Segmentation-Keras](https://github.com/TianzhongSong/Person-Segmentation-Keras)
- "HeadShoulderData" is the Flickr Portrait Dataset, fetched using [Insight Project](https://github.com/jmlb/insight_project)

