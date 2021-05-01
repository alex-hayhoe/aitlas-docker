from marshmallow import Schema, fields, validate


class BaseDatasetSchema(Schema):
    batch_size = fields.Int(missing=64, description="Batch size", example=64)
    shuffle = fields.Bool(
        missing=True, description="Should shuffle dataset", example=False
    )
    num_workers = fields.Int(missing=4, description="Number of workers", example=4)
    pin_memory = fields.Bool(
        missing=False, description="Whether to use page-locked memory"
    )
    transforms = fields.List(
        fields.String, missing=None, description="Classes to run transformations.",
    )
    target_transforms = fields.List(
        fields.String, missing=None, description="Classes to run transformations.",
    )
    labels = fields.List(
        fields.String, missing=None, description="Labels for the dataset",
    )


class BaseModelSchema(Schema):
    num_classes = fields.Int(missing=2, description="Number of classes", example=2)
    use_cuda = fields.Bool(missing=True, description="Whether to use CUDA if possible")
    metrics = fields.List(
        fields.String,
        missing=["f1_score"],
        description="Metrics you want to calculate",
        example=["accuracy", "precision", "iou"],
        validate=validate.ContainsOnly(
            ["accuracy", "precision", "recall", "f1_score", "iou"]
        ),
    )
    weights = fields.List(
        fields.Float,
        missing=None,
        description="Classes weights you want to apply for the loss",
        example=[1.0, 2.3, 1.0],
    )


class BaseClassifierSchema(BaseModelSchema):
    learning_rate = fields.Float(
        missing=None, description="Learning rate used in training.", example=0.01
    )
    pretrained = fields.Bool(
        missing=True, description="Whether to use a pretrained network or not."
    )
    threshold = fields.Float(
        missing=0.5, description="Prediction threshold if needed", example=0.5
    )


class BaseSegmentationClassifierSchema(BaseClassifierSchema):
    metrics = fields.List(
        fields.String,
        missing=["iou"],
        description="Classes of metrics you want to calculate",
        example=["accuracy", "precision", "recall", "f1_score", "iou"],
    )


class BaseTransformsSchema(Schema):
    pass
