/*

  the prefix `_i` denotes an inferred predicate
  
*/

% ========================================
% model-level reasoning
% ========================================

subclass_of(C,D) :- proper_subclass_of(C,D).
subclass_of(C,C) :- class(C).
direct_subclass_of(C,D) :- is_a(C,D),class(C),class(D).
direct_subclass_of(C,D) :- mixin(C,D),class(C),class(D).
proper_subclass_of(C,D) :- direct_subclass_of(C,D).
proper_subclass_of(C,D) :- direct_subclass_of(C,Z), proper_subclass_of(Z,D).

class_disjoint_with(C,D) :- is_a(C,Z),is_a(D,Z), C\=D, class(Z), \+ is_mixin(Z).


subrelation_of(C,D) :- proper_subrelation_of(C,D).
subrelation_of(C,C) :- slot(C).
direct_subrelation_of(C,D) :- is_a(C,D),slot(C),slot(D).
direct_subrelation_of(C,D) :- mixin(C,D),slot(C),slot(D).
proper_subrelation_of(C,D) :- direct_subrelation_of(C,D).
proper_subrelation_of(C,D) :- direct_subrelation_of(C,Z), proper_subrelation_of(Z,D).

i_domain(R,D) :- domain(R1,D1), subrelation_of(R,R1), subclass_of(D1,D).
i_range(R,D) :- range(R1,D1), subrelation_of(R,R1), subclass_of(D1,D).

i_domain_in(R,D,C) :- i_domain(R,D),class(C).
i_domain_in(R,D,C) :- domain_in(R1,D1,C1),subrelation_of(R,R1), subclass_of(D1,D),subclass_of(C,C1).
i_range_in(R,D,C) :- i_range(R,D),class(C).
i_range_in(R,D,C) :- range_in(R1,D1,C1),subrelation_of(R,R1), subclass_of(D1,D),subclass_of(C,C1).

unsatisfiable(C) :- subclass_of(C,A),subclass_of(C,B),class_disjoint_with(A,B).

incoherent :- unsatisfiable(_).
incoherent :- inconsistent(_).

% ========================================
% instance-level reasoning
% ========================================


% bridge to URIs. For convenience we allow use of symbols instead of URIs
direct_instance_of(I,C) :- rdf(I,rdf:type,Cx), has_uri(C,Cx).
direct_instance_of(I,C) :- rdf(I,rdf:type,C).

instance_of(I,C) :- direct_instance_of(I,C1), subclass_of(C1,C).

direct_fact(I,P,J) :- rdf(I,Px,J), has_uri(P,Px), \+ rdf(I,rdf:type,J).
direct_fact(I,P,J) :- rdf(I,P,J), \+ rdf(I,rdf:type,J).

inconsistent(I) :- instance_of(I,C),unsatisfiable(C).

invalid(I) :- direct_fact(I,P,_), \+ ((instance_of(I,IC), subrelation_of(P, PA), class_slot(IC, PA) )).

% note that this is different than OWL, as we adopt a closed world interpretation.
% an instance is invalid if it is inferred to instantiate a class C through domain or range constraints
% AND it is not inferred to be of that class via OO rules
invalid(I) :- domain_induced_instance_of(I,C),\+ instance_of(I,C).
invalid(I) :- range_induced_instance_of(I,C),\+ instance_of(I,C).

domain_induced_instance_of(I,C) :- direct_fact(I,P,_), instance_of(I,C1),i_domain_in(P,C,C1).
range_induced_instance_of(I,C) :- direct_fact(_,P,I), instance_of(I,C1),i_range_in(P,C,C1).


