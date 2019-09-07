all: test

TESTS = $(patsubst %_test, %, $(patsubst tests/%, %, $(basename $(shell ls tests/*_test.pro))))

test: $(patsubst %,test-%, $(TESTS))

test-%:
	./tests/run-test.sh tests/$*_test.pro

tests/biolink.pro: 
	cd .. && pipenv run python3 biolinkml/generators/lpgen.py tests/test_biolink_model/yaml/biolink-model.yaml > $@


x:
	echo $(TESTS)
