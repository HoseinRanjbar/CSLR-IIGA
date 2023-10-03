# Continuous Sign Language Recognition Using Intra-Inter Gloss Attention

This repository provides a pytorch-based implementation of **Continuous Sign Language Recognition Using Intra-Inter Gloss Attention**.


Sign languages are the primary communication medium of the hearing-impaired people. Mastering this language is rather difficult
for the hearing people, thus hindering direct communications between two groups. Sign Language Recognition provides a bridge to
overcome this gap. Our propose model consists of three modules : the visual module (MobileNet-V2), the sequential module(Transformer)
and the alignment module(CTC). This work represents the first attempt in the field of continuous sign language recognition
to incorporate an intra-inter gloss attention module. These two modules are embedded within the sequential module and used in
place of the vanilla self-attention module.

**Overview of our propose model is provided in below.**


