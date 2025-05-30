---
title: Privately sharing restricted-access data with the AEA Data Editor
toc: true
date: 2021-04-08
---

In certain cases, you may be able to share data you obtained from somebody ("data provider") with the AEA Data Editor for the purpose of conducting reproducibility checks, without later publishing the data ("privately sharing data").  

> If you are able to more broadly share sensitive data with any user who can provide, for instance, IRB approval, please see [this other guide on creating a separate data deposit](creating-separate-data-deposit).

Note that the ability to privately provide the data does not preclude the possibility that others, including the Data Editor, may independently request access to the data from the data provider. Private provision is sometimes the only way the Data Editor can access the data. At other times, it is simply a more expedient or timely way to provide the data. Authors should be clear about describing **both** options when both are available.

This page describes some tips and methods of doing so, and considerations. Please read it carefully.

### DO's and DON'Ts

- Do NOT transfer data that you have no rights to transfer. Always carefully read your data use agreement (DUA), license, or non-disclosure agreement (NDA) that you signed.
- Do NOT upload the restricted-access data to openICPSR. 
- DO structure the repository to take into the account the data that cannot be published. See this [note](https://aeadataeditor.github.io/aea-de-guidance/preparing-for-data-deposit.html#structure-in-the-presence-of-confidential-unpublished-data).

### Permissions

First and foremost, you must have the rights to *privately* share data. This will be noted in the data use agreement (DUA), license, or non-disclosure agreement (NDA) that you signed to obtain access to the data from the data provider. In general,

- if you signed an NDA, it is unlikely that you are allowed to automatically share data with others. However, the AEA Data Editor may sign the same or a similar NDA with the data provider. Note that this should always be noted in the **public** README, as this may also apply to any other future replicator.
- if you signed a DUA, read it carefully, as it may explicitly allow or deny you right to redistribute the data. 
  - In some cases, you may need to explicitly ask your data provider. Some will allow data to be shared privately between subscribers (examples in the past have included S&amp;P and Bureau Van Dijk, but you should ask). The AEA Data Editor may be able to facilitate the conversation.
- if the data you obtained (via download or purchase) had a license attached to it, read it carefully. Common licenses include CC-BY and variants thereof, which allow for redistribution. Others may not. 
- you may have acquired full rights to the data, by collecting it yourself (but careful: participant consent!) or by outright purchasing the data. However, not every purchase gives you full rights to the data! Read your purchase agreement (license).
- In some cases, data usage rights may apply to your "research group" or your "institution." It may be possible to temporarily include the AEA Data Editor as a member of your "research group" for the purpose of conducting reproducibility checks. In other cases, rights are automatically granted to anybody within your institution (your agency, company, or university) while at the same time automatically being limited to that same institution. 

If your data use agreement, license, or non-disclosure agreement does not seem to allow to share the data with the Data Editor, you can ask your data provider explicitly to allow you to do so, or to share directly with the Data Editor. Sample text:

> The AEA is conducting a reproducibility check for my manuscript entitled "X." Would it be possible for you to allow us to provide the restricted-access data to the AEA Data Editor so that he may proceed to verify the reproducibility of the entire replication package? The data would not be published, and would be deleted by the Data Editor once he has completed the process.

You can point them to this page for more information.

### Documenting restrictions and instructions

Whatever restrictions are imposed on the data typically convey to other replicators as well. All restrictions should be documented in the published README, in the section about "[Data Availability and Provenance Statements](https://social-science-data-editors.github.io/template_README/template-README.html#data-availability-and-provenance-statements)."

If you filled out an application form, it may be useful to include the filled-out application form with the replication package, or to provide the information needed for a replicator to fill out the application form. The AEA Data Editor may need the same information to acquire data that you cannot share directly.

### Signaling availability

AEA authors are required to submit a [Data and Code Availability Form](https://www.aeaweb.org/journals/forms/data-code-availability), which has an option to signal the ability to privately provide data to the AEA Data Editor. Please alert the editor as early as possible about this - in most cases, agreements can take a while to put in place. Note that the ability to privately provide the data does not preclude the possibility that others, including the Data Editor, may independently request access to the data from the data provider. Please check all options that apply!

### Sharing data with Data Editor

#### Preferred contractual arrangement

The AEA Data Editor is an employee of an educational institution, not the AEA itself (see [main page](https://aeadataeditor.github.io/) for the current AEA Data Editor's affiliation). Thus, all access rights are constrained by rules at that educational institution. 

- If an NDA needs to be signed, the use of [Cornell’s Individual Standard Non-Disclosure Agreement](https://researchservices.cornell.edu/resources/standard-individualunilateral-non-disclosure-agreement-nda) (as of 2021) is the most time-efficient. Deviations thereof may need approval by the host institution's office of sponsored research and may delay signature of the agreement.
- If the AEA Data Editor needs to request the data from the original data provider independently, you should provide enough information to fill out all required forms.

- If IRB approval was required for you to access the data, then there are a few considerations to take into account. 

    - In general, the AEA Data Editor does **not** need separate IRB approval, since the work of the AEA Data Editor does not constitute "engagement" (formal involvement in research) because, as described in 45CFR46 (Common Rule) "*the services performed do not merit professional recognition or publication privileges*" [[1](https://www.hhs.gov/ohrp/regulations-and-policy/guidance/guidance-on-engagement-of-institutions/index.html)] (the AEA Data Editor does not publish any of the work they conduct as part of the reproducibility checks)
    - However, in some cases, the data provider may still require formal consideration by the IRB at the AEA Data Editor's institution. Our IRB (at this time, Cornell University) has agreed to review such requests if necessary. 

#### Preferred data access

- If the data do not contain personal identifiers, then in general, transfer is straightforward, but check with your DUA/NDA/IRB approval/exemption. 
- The AEA Data Editor uses IT systems that are university-controlled, with access protected by VPN and individual sign-on, both using 2FA. 
- If the data do require higher security protocols, the AEA Data Editor has access to [high-security remote-access environments at Cornell University](https://ciser.cornell.edu/data/secure-data-services/cradc/), though setting up access may require additional time (and may require approval by Cornell's Office of Sponsored Research).

#### Mechanics of data transfer

- All data transfers should be compliant with your DUA/NDA.
- By default, if you have signalled that you can provide data privately, the Data Editor will send you an email containing a link to a secure upload form, where you can provide the data
- You can share data with the AEA Data Editor using other means, such as your own Dropbox, Google Drive, OneDrive, etc. subscription.
- If necessary, you can also provide the AEA Data Editor with remote access to your own computing infrastructure (remote login to compute nodes or virtual enclaves).

All of these methods have been successfully used in the past.


