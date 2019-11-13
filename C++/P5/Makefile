CXXFLAGS += --std=c++17

debug: CXXFLAGS += -g

all: test

test: P5.cpp
	 $(CXX) $(CXXFLAGS) P5.cpp -o test

clean:
	-rm -f *.o *.gch *~ a.out test *.txt

