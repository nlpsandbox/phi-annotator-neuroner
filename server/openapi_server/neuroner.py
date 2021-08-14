from neuroner import neuromodel

class Neuroner:
    def __init__(self):
        self.model = None

    def initialize(self):
        self.model = neuromodel.NeuroNER(
            train_model=False,
            use_pretrained_model=True,
            dataset_text_folder="data/example_unannotated_texts",
            pretrained_model_folder ="data/trained_models/i2b2_2014_glove_spacy_bioes",  # noqa: E501
            parameters_filepath='.',
            spacylanguage="en_core_web_sm",
            token_pretrained_embedding_filepath='data/word_vectors/glove.6B.100d.txt',  # noqa: E501
            load_all_pretrained_token_embeddings=1,
            maximum_number_of_epochs=500
        )

    def annotate(self, text):
        if self.model is None:
            self.initialize()
        return self.model.predict(text)


neuroner = Neuroner()