from enum import unique
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CandidateRule(Base):
    __tablename__ = "candidate_rules"

    counter = Column(String(50), primary_key=True)
    id = Column(Integer, index=True)
    antecedent = Column(Text)
    consequent = Column(Text)
    package_id = Column(Integer, ForeignKey("candidate_rule_packages.id"))
    package = relationship("CandidateRulesPackage", back_populates="candidate_rules")


class CandidateRulesPackage(Base):
    __tablename__ = "candidate_rule_packages"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255))
    candidate_rules = relationship("CandidateRule", back_populates="package")


class LabeledRule(Base):
    __tablename__ = "labeled_rules"

    id = Column(String(50), primary_key=True)
    candidate_rule_id = Column(Integer, nullable=False)
    rule_description = Column(Text, nullable=False)
    label = Column(String(15), nullable=False)
    user_id = Column(String(50), ForeignKey("users.id"))

    user = relationship("User")


class User(Base):
    __tablename__ = "users"

    id = Column(String(50), primary_key=True)
    name = Column(String(256), nullable=False)