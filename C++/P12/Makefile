CXXFLAGS += --std=c++17

debug: CXXFLAGS += -g

all: solution

test: all
	./solution | tee result.txt

solution: P12.cpp
	 $(CXX) $(CXXFLAGS) P12.cpp -o solution

clean:
	-rm -f *.o *.gch *~ a.out solution *.txt

