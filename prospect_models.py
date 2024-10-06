from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text
from typing import List, Optional

class Base(DeclarativeBase):
    pass


class Prospect(Base):
    __tablename__ = 'prospects'
    id: Mapped[int] = mapped_column(primary_key = True)
    first_name: Mapped[str] = mapped_column(nullable = False)
    last_name: Mapped[str] = mapped_column(nullable = False)
    age: Mapped[int] = mapped_column(nullable = False)
    region_id: Mapped[int] = mapped_column(nullable = False)#mapped_column(ForeignKey('regions.id'))
    subregion_id: Mapped[int]
    height: Mapped[int]
    weight: Mapped[int]
    bats: Mapped[int]
    throws: Mapped[int]
    prestige:Mapped[int] #2-5 star
    makeup_id:Mapped[int]

    #one to one
    attributes:Mapped[List["Attributes"]] = relationship(back_populates = 'prospect')
    #one to one
    performance:Mapped[List["Performance"]] = relationship(back_populates = 'prospect')
    # one to one
    pos_played = relationship("PositionsPlayed", back_populates = 'prospect', uselist = False)
    #one to many
    pitches:Mapped[List["Pitch"]] = relationship(back_populates = 'prospect')

    inj_history:Mapped[List["InjuryHistory"]] = relationship(back_populates = 'prospect')



    def __repr__(self) -> str:
        return f"<Prospect Name={self.first_name} {self.last_name}>"

class Attributes(Base):
    __tablename__ = 'attributes'
    prospect_id: Mapped[int] = mapped_column(ForeignKey('prospects.id', ondelete = 'CASCADE'), primary_key = True)
    direct_to_ball: Mapped[int]
    plate_vision: Mapped[int]
    baseball_movements: Mapped[int]
    explosiveness: Mapped[int]
    strength: Mapped[int]
    rotationality: Mapped[int]
    max_frame: Mapped[int]
    home_first: Mapped[int]
    sixty_yd: Mapped[int]
    velo_of: Mapped[int]
    velo_if: Mapped[int]
    arm_consistency: Mapped[int]
    framing: Mapped[int]
    pop_time: Mapped[int]
    agility: Mapped[int]
    adaptability: Mapped[int]
    velo_fb: Mapped[int]
    velo_ch: Mapped[int]
    velo_bb: Mapped[int]
    experience: Mapped[int]
    pos_feel: Mapped[int]
    catcher_feel: Mapped[int]
    #max health level
    durablity: Mapped[int]
    availability: Mapped[int]
    # 70 / 26 / 4
    pro_super_split: Mapped[int]
    #Level a player can play unaffected by their injury
    prospect:Mapped["Prospect"] = relationship(back_populates = 'attributes')


class Performance(Base):
    __tablename__ = 'performance'
    prospect_id: Mapped[int] = mapped_column(ForeignKey('prospects.id'), primary_key = True)
    games_played: Mapped[int]
    hits_per_pa: Mapped[int]
    at_bats: Mapped[int]
    home_runs: Mapped[int]
    stolen_bases: Mapped[int]
    batter_walks: Mapped[int]
    batter_sos: Mapped[int]
    batter_xbh: Mapped[int]
    errors: Mapped[int]
    prospect:Mapped["Prospect"] = relationship(back_populates = 'performance')
    

class PositionsPlayed(Base):
    __tablename__ = 'positions_played'
    id: Mapped[int] = mapped_column(primary_key = True)
    prospect_id: Mapped[int] = mapped_column(ForeignKey('prospects.id'))
    pos_1: Mapped[int]
    pos_2: Mapped[int]
    pos_3: Mapped[int]
    pos_4: Mapped[int]
    pos_5: Mapped[int]
    prospect: Mapped["Prospect"] = relationship("Prospect", back_populates = 'pos_played')

    def __str__(self):
        return "Test"
    


class Pitch(Base):
    __tablename__ = 'pitches'
    id: Mapped[int] = mapped_column(primary_key = True)
    prospect_id: Mapped[int] = mapped_column(ForeignKey('prospects.id'))
    pitch_type_id: Mapped[int]
    spin_rate: Mapped[int]
    spin_eff: Mapped[int]
    hand_position: Mapped[int]
    velo_consistency: Mapped[int]
    mound_pos: Mapped[int]
    release_x: Mapped[int]
    release_y: Mapped[int]
    v_movement_sharpness: Mapped[int]
    delivery_eff: Mapped[int]
    horizontal_movement: Mapped[int]
    h_movement_sharpness: Mapped[int]
    pitch_sub_id: Mapped[int]
    prospect:Mapped["Prospect"] = relationship(back_populates = 'pitches')

    def __str__(self):
        print("Fastball")
    

class InjuryHistory(Base):
    __tablename__ = 'injuries'
    id: Mapped[int] = mapped_column(primary_key = True)
    prospect_id: Mapped[int] = mapped_column(ForeignKey('prospects.id'))
    duration: Mapped[int]
    severity: Mapped[int]
    prospect: Mapped["Prospect"] = relationship("Prospect", back_populates = 'inj_history')

    
class Scout(Base):
    __tablename__ = 'scouts'
    id: Mapped[int] = mapped_column(primary_key = True)
    first_name: Mapped[str] = mapped_column(nullable = False)
    last_name: Mapped[str] = mapped_column(nullable = False)
    home_region:Mapped[int]
    team_id: Mapped[int]
    archetype_id: Mapped[int]
    caa_percentage: Mapped[int]
    prestige: Mapped[int]
    assigned_region: Mapped[int]
    #ScoutingReport
    visit_increase: Mapped[int]


class ScoutingReport(Base):
    __tablename__ = 'scouting_reports'
    id: Mapped[int] = mapped_column(primary_key = True)
    scout_id: Mapped[int] = mapped_column(ForeignKey('scouts.id'))
    prospect_id: Mapped[int] = mapped_column(ForeignKey('scouts.id'))
    visit_count: Mapped[int]
    hit_tool: Mapped[int]
    game_power: Mapped[int]
    raw_power: Mapped[int]
    speed: Mapped[int]
    defense: Mapped[int]
    plate_discipline: Mapped[int]
    #list of makeup objects
    makeup_id: Mapped[int]
    #list of projection objects
    projection_id: Mapped[int]
    hitter_level: Mapped[int]
    #list of projection objects
    position_projection: Mapped[int]
    #list of projection objects
    max_frame: Mapped[int]
    stuff: Mapped[int]
    starter_or_reliever: Mapped[bool]
