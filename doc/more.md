
___

Theories
===
What are academic disciplines?


The philosophical perspective unity and pluralism
The anthropological perspective culture and tribes
The sociological perspective professionalization and division of labour
The historical perspective evolution and discontinuity
The managment perspective market and organization

Survival strategoes for disciplines
[Krishnan]

```
fit_of_perspective(dsc, perspective)
is_borrowed(cnc)
is_psychological_warfare_concept(cnc)
```
___
Structuring of Research Fields
--
* polycentric oligarchy - in which a handful of researchers occupy dominating positions and create rival schools, using their own results assessment methods. Examples: ’German psychology at the start of the twentieth century and British social anthropology.
* partitioned bureaucracy - standardised training programmes, relative theoretical cohesion and a focus on analytical work (very little control of empirical phenomena). Anglo- Saxon neoclassical economics, which operates like a 
* Fragmented adhocracy: without any kind of collective direction or overall consistency, coalitions in the fi eld are temporary. Objects are defi ned outside of the discipline according to the audience. Example: British sociology and literary studies. 
* Professional adhocracy: coordination of research resources for multiple objects and projects, according to audience and infl uence. Example: biomedical sciences.
* Polycentric profession: common working procedures act as a framework for controversies in the fi eld. Example: experimental physiology.
* Technologically integrated bureaucracy: coordination of work using the same set of instruments, methods and concept (nomenclature). Knowledge is both empirical and specifi c. Example: chemistry.
* Conceptually integrated bureaucracy: coordination of work via a unifi ed theoretical framework establishing the hierarchy of specialities. Example: physics. (last five by Whitley)

Such functions may be developed as:

```
is_polycentric_oligarhy(dsc)
is_partinioned_beurocracy(dsc)
is_fragmented_adhocracy(dsc)
is_professional_adhocracy(dsc)
is_polycentric_profession(dsc)
is_technologically_integrated_bureaucracy(dsc)
is_conceptually_integrated_bureaucracy(dsc)
```

___
Power strugles 
---
Border wars: for example, between molecular biology and cellular biology.
- Wars of conquest and hegemony where, each in turn, theology, physics, molecular biology, sociology,1 economics, sociobiology,2 neurosciences,3 and so on, believe they can rule over all or part of the fields of knowledge, either by setting up a skilful division of labour, or by making sure they are well placed in the tree of knowledge, or by imposing
the right scientific method on all the others. The temptation at times is to isolate a metatheory (as a systemic theory) or an interdisciplinary science in a quest for a new unity of all sciences, even including religions too.
- Despoilment where the idea is to take over a concept from a related discipline and reformulate it so that it fi ts with one’s own discipline.
- Attempts at eradication: for example, in the cognitive sciences, the proclamations by the neurosciences of the forthcoming end of cognitive psychology.
- Caricature, simplification and instrumentalisation: researchers apply the problems and practices of their own disciplines in order to perceive other disciplines. They confer on these disciplines a role and an image that do not fit.
Economic war when the authorities in charge of allocating resources (posts, subsidies, equipment and premises), take action to weaken rival disciplines for the benefit of their own discipline. This is how disciplines like botany, zoology and physiology came to be in a state of collapse at the end of the 1960s because the scientific managers of the French
CNRS redeployed their resources to molecular biology, hence placing other disciplines below the survival threshold.
- Psychological war and war of attrition when, without meaning to have a negative effect, some people repeatedly use terms such as ‘soft sciences’ when referring to the social sciences, which, in turn, retaliate with a less effective ‘inhuman sciences’.

(Vinck 73)

The key concepts are *believe they can rule over all or part of the fields of knowledge*, *setting up a skilful division of labour*, *making sure they are well placed in the tree of knowledge*, *imposing the right scientific method*. Here we have to make a separation between aims and strategies. The easiest one to follow is *well placed in the tree of knowledge*, it refers to positioning in various classifications, belonging to right faculties and etc. it is also rather not that expensive to find whether a discipline is *imposing the right scientific method*.

*Taking over a concept from other discipline and reformulate* - true, happens, easy to do.
We can understand what is *attempts at eradication* by investigating case *neurosciences vs cognitive psychology*

*Caricature*, *simplification* and *instrumentalisation*... Alocation of resources (posts, subsidies, equipment and premises) are rather easy to find. we can built on cases mentioned by Vinck, *molecular biology vs. botany, zoology and physiology*. 

Psychological warfare and war of attrition is ok to find use of such terms as *soft sciences* or *inhuman sciences*. However, it might much harder to identify such terms. Still, it is possible by conducting interviews.

Such functions may be developed as:

```
where_in_tree_of_knowledge(dsc, tree)
is_borrowed(cnc)
is_psychological_warfare_concept(cnc)

```

___
Justifications for interdisciplinary work
----
- Scientific creativity:
- Conquest:
- Relevance of scientific work in relation to the object or issue at stake:
- Concrete research work:

It is hard to identify the justifications. However, one might be found in a) interviews, b) introductions, c) cvs
[Vinck 74]

```
justification_for_interdisciplinary_work(author)
is_justification_scientific_creativity()
is_justification_conquest()
is_justification_relevence_of_scientific_work()
is_justification_concrete_research_work()
```

___
Regimes of Knowledge Production
---
- The disciplinary regime
- The transitory regime:
- The utilitarian regime
- The transverse regime

To find out regime of a discipline one must identify disciplinary formulation first.

```
regimes_for_knowledge_production(dsc) #returns a dictionary of regimes and associated values
is_regime_disciplinary(dsc)
is_regime_transitory(dsc)
is_regime_utilitarian(dsc)
is_regime_transverse(dsc)

```

___
Characterisation of organisational structures
--

1. Functional dependence (FD): the different types of knowledge produced rely on
each other. When there is a high level of FD, teams use the same procedures and
link up their results. When it is low, the procedures vary and the results are not
cumulative.
2. Strategic dependence (SD): work depends on the defi nition of collective research
priorities and the allocation of resources. When SD is high, teams rival with each other
in order to control resources and recognition in the fi eld, including control over the
name given to the fi eld. When it is low, teams are less concerned with the hierarchy of
objectives across the field.

| |Low functional dependence |High functional dependence |
|----|---|----|
| Low strategic dependence | Anarchy of the teams pursuing different goalswith different methods, without either coordinationor division of labour?|Pacific coexistence of specialised teams working with standardised methods and coordinating their work but without imposing any structure to their research field|
| High strategic dependence | Fight between schools of thinking for thedomination of the discipline. Teams internally coordinated but pursuing different goals and|Fight between subdisciplines (using the same procedures and coordinating their work) for control and the hierarchy inside the discipline |


The core notion of teams, methods and strategy. The hook here is *standardised methods*, while it is very hard to identify *imposing structure to the research field*. A term like *pacific coexistence of specialised teams* is hard to identify, but maybe possible. There seems to be a overarching meaning between concepts of *teams* and *schools*, however, we might consider *schools* as somewhat more formed and distinct than *teams*. Also, how to identify *fight for domination* maybe it is possible to do that. The *fight between disciplines for control and hierarchy inside disciplines* is similar to *fight fo domination* but refers to different kind of fight.


```
get_standard_methods(dsc)
is_standard_method(mth, dsc)
is_imposing_structure_to_the_research_field(dsc)
is_pacific_coexistence_of_specialised_teams(dsc)
get_specialised_teams(dsc)
is_school(name)
is_team(name)
is_fighting_for_domination(dsc) #second may be added
```


[Whitley, 1974] f
[Vinck]ff

___

Several interdisciplinary models
--

* The complementarity model: linking up of complementary skills to form a joint approach to an issue. Rather than just simply juxtaposing disciplinary contributions, the different points at which knowledge is linked up are explored with the aim of making a joint achievement (analysis, problem- solving, use of an experimental instrument). One of the disciplines sometimes plays a leading role, with the risk of instrumenting the others. Disciplinary cleavages are reproduced without displacing the researcher’s identity. Sometimes, the protagonists become aware of the limits of their discipline and hence query the divisions and feel the need to revise their conceptual approaches.
* The circulation model: researchers belonging to one discipline explore others in order to borrow their concepts, methods, questions or problems to be solved. Lavoisier thus imported tools and methods from experimental physics for the purposes of chemistry; the École des Annales (French school of annals), did the same for history, by opening up to economics, sociology and then anthropology. The receiving discipline is itself sometimes structured around several specialities according to the imports made. Pre- history provides an excellent example of this as it draws its resources from anatomy, technology, ecology, genetics, ethology, psychology, sociology, anthropology, chemistry and physics (dating techniques), climatology, botany and zoology.
* The fusion model: grouping together of researchers working on the same object, attenuating the distinctions between the initial disciplines. Ecology is an example of a speciality born from the merging of several types of knowledge around an object and concepts such as niche and ecosystem. It brings together knowledge from botany, zoology, pedology and orography. The new speciality reconfi gures the identity of researchers around a new reference. In other cases, this reconfiguration only leads to a vague assembly that fails to be recognised from an institutional point of view.
* The confrontation model: where existing disciplines enter into debate. The, at times, cutting interactions have a backlash effect on the disciplines: repatriation of joint productions and shifts during confrontations.

Regarding complemntarity model - when one discipline is playing leading role? When protagonists *revice their conceptual approaches*.
Regarding the circulation model. borrowing concept, borrowing method, borrow question, borrow problem. We are happy to know that Lavosier was the case, French school of anals. But the best comes from history with its relations with from anatomy, technology, ecology, genetics, ethology, psychology, sociology, anthropology, chemistry and physics (dating techniques), climatology, botany and zoology.
Regarding the fusion model. 

```
interdisciplinary_model(dsc) #returns kind of interdisciplinary model
is_model_complementary(dsc)
    is_approach_joint
    
is_model_circulation(dsc)
    is_researcher_exploring_others_to_borrow_concepts(rsc)
    is_structured_around_imports(dsc)
is_model_fusion(dsc)
    is_approach_recognised_by_institution(approach, institution)
is_model_confrontation(dsc)
    are_confronting(dsc_list)

```

___
The Emergence 
--
(Ziman, 1987)
1. Emerging specialty is only observable as a nodal point in the network of citations.
2. Scientists whose research is associated with this co-citation cluster organize little research conferences to discuss their common interests, or are commissioned to write articles for a special issues of a primary journal drawing attention to progress in this particular problem area.
3. An ‘invisible college’ begins to condense out, in the form, say, of a semi-official association held together by further conferences, the regular exchange of pre-prints and re-prints and the publication of an informal ‘newsletter’.
4. The association develops into a regular learned society, whose newsletter has become a reputable primary journal.
5. A hierarch of authority is soon set up to preside over conferences, edit journals, allocate resources, and confer recognition on the members of the new discipline.

The object of analysis is easy to specify when it comes to first point. It is some citations.
In second point we have to identify a) scientists associated with citation cluster, b) conferences. Or and to look for special issues of primary journals.
It is hard to identify third point as we would need to find "invisible college", exchange of pre-prints nadd reprits. But, it is possible to find some newsletters. The fourth step is straightforward, it is rather easy to identify learned society when it already exists, the same about the journal. The fifth. Who presides over conferences, who edit journal and who allocate resources and confer recognition is easy to get. Most of this information can be get online.

Several strategies are available to do such things. It depends what we want to do. The later stage of development the easier is to get data. However, even when it comes to finding NPNOC it can be accomplished.

Other thing to consider is the starting point of research. Whether to start from specific disciplines or just run over all. The first type is easier to do, but then we would come to a problem of integrating the data. The second approach is harder to do but is better one. For know, I think the best way to go is to have small case studies, built on earlier research, and follow by constructing the overarching algorithms.

Functionality: identification of turning points of development of a discipline by identifying NPNOC, people, conferences and etc date is the prime focus.

```
interdisciplinary_model(dsc) #returns kind of interdisciplinary model
what_emergence_state(dsc)
is_emergence_state(dsc, stage)
```


___
Taxonomy of Interdisciplinarity
--
Klein


```
is_multidisciplinary(what, by_whom)
is_juxtaposing()
is_sequencing()
is_coordinating()

is_interdisciplinary()
is_integrating()
is_interacting()
is_linking()
is_focusing()
is_blending()

is_transdisciplinary(what, by_whom)
is_transcending()
is_transgressing()
is_transforming()

is_encyclopeadic()
is_pseudo(what)
is_indiscriminate(what)

is_systematic_integration()
is_transsector_interaction()

is_partial_integration()
is_contextualizing()
is_auxiliary()
is_composite()

is_full_integration()
is_conceptual
is_structural_or_unifying()
is_integrative

is_inbetween_partial_and_full_integration() #derived is_suplementary()
is_generalizing()

is_monodisciplinary(what, by_whom)
is_pluridisciplinary(what, by_whom)

degree_of_collaboration()
""" returns shared or cooperative """
is_degree_of_collaboration_shared()
is_degree_of_collaboration_cooperative()

is_narrow()
is_wide()
is_broad()

is_methodological()
is_theoretical()

is_bridge_building()
is_restructuring()

is_instrumental()
is_critical()

is_endogenous()
is_exogenous()
```

___
Overview
==

A discipline is what is being described as a discipline by those who study disciplines.

Within theorie we have a list of disciplines that were mentioned.
